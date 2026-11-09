#!/usr/bin/env bash
# Week 5 Lab 1 pipeline:
#   deps (cached) -> test -> build -> load -> canary -> bake -> gate -> promote | rollback
# Usage:
#   ./pipeline.sh --ci-only      deps + test only (no Docker needed)
#   ./pipeline.sh                full run against the kind cluster
set -euo pipefail
cd "$(dirname "$0")"

CLUSTER="${KIND_CLUSTER:-w5}"
CACHE_DIR="${CACHE_DIR:-$PWD/.cache}"
BAKE_SECONDS="${BAKE_SECONDS:-10}"
MODE="${1:-}"

stage() { printf '\n== %s ==\n' "$1"; T0=$SECONDS; }
took()  { printf '   (%ss)\n' $((SECONDS - T0)); }
record() { printf '%s %s %s\n' "$(date -u +%FT%TZ)" "$1" "$2" >> releases.log; }

# ---- 1. deps, cached. The key must change whenever an input that changes the result changes.
stage "deps"
PYV="$(python3 -c 'import sys; print("%d.%d" % sys.version_info[:2])')"
CACHE_KEY="deps-py${PYV}-$(shasum -a 256 app/requirements-dev.txt | cut -c1-12)"
VENV="$CACHE_DIR/$CACHE_KEY"
if [[ -x "$VENV/bin/pytest" ]]; then
  echo "cache HIT  $CACHE_KEY"
else
  echo "cache MISS $CACHE_KEY"
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -q --disable-pip-version-check -r app/requirements-dev.txt
fi
took

# ---- 2. test
stage "test"
(cd app && "$VENV/bin/pytest" -q -p no:cacheprovider)
took
if [[ "$MODE" == "--ci-only" ]]; then echo "ci-only: stopping before build"; exit 0; fi

# ---- 3. build once. Tag = hash of the inputs: same source -> same tag -> same artifact everywhere.
stage "build"
TAG="$(cat app/Dockerfile app/server.py | shasum -a 256 | cut -c1-10)"
docker build -q -t "web:$TAG" app
echo "artifact web:$TAG"
took

# ---- 4. ship the artifact to the cluster's nodes (a registry push, in real life)
stage "load"
kind load docker-image "web:$TAG" --name "$CLUSTER" >/dev/null
took

render() { sed "s/IMAGE_TAG/$TAG/g" "$1"; }

# First run ever: no stable track yet, so it becomes stable directly.
if ! kubectl get deploy/web-stable >/dev/null 2>&1; then
  stage "bootstrap stable"
  render k8s/stable.yaml | kubectl apply -f -
  kubectl rollout status deploy/web-stable --timeout=180s
  record "$TAG" BOOTSTRAP
  took; exit 0
fi

CURRENT="$(kubectl get deploy/web-stable -o jsonpath='{.spec.template.spec.containers[0].image}')"
CURRENT="${CURRENT#web:}"
if [[ "$CURRENT" == "$TAG" ]]; then echo "stable already runs web:$TAG, nothing to ship"; exit 0; fi

rollback() {
  echo "ROLLBACK: deleting canary web:$TAG; stable stays on web:$CURRENT"
  kubectl delete deploy/web-canary --wait=true >/dev/null
  record "$TAG" "ROLLED_BACK($1)"
  exit 1
}

# ---- 5. canary: 1 pod next to 9 stable pods behind one Service, so about 10% of traffic
stage "canary"
render k8s/canary.yaml | kubectl apply -f -
kubectl rollout status deploy/web-canary --timeout=90s || rollback "canary-not-ready"
took

# ---- 6. bake, then gate on what users would see (not on the readiness probe)
stage "bake ${BAKE_SECONDS}s"
sleep "$BAKE_SECONDS"
took

stage "gate"
if [[ ! -x ./canary_gate.sh ]]; then
  echo "canary_gate.sh is missing or not executable: write it (spec in the Week 5 pack, Lab 1)"
  rollback "no-gate"
fi
CANARY_VERSION="$TAG" STABLE_VERSION="$CURRENT" ./canary_gate.sh || rollback "gate-failed"
took

# ---- 7. promote the SAME artifact to stable, then retire the canary
stage "promote"
render k8s/stable.yaml | kubectl apply -f -
kubectl rollout status deploy/web-stable --timeout=180s
kubectl delete deploy/web-canary >/dev/null
record "$TAG" PROMOTED
echo "PROMOTED web:$TAG (was web:$CURRENT)"
took
