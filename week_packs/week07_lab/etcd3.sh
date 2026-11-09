#!/usr/bin/env bash
# Week 7 Lab 2: a local 3-node etcd cluster you can break.
# Usage: ./etcd3.sh start | status | kill N | up N | stop | clean
#   start   start n1, n2, n3 (fresh cluster)
#   status  leader, term and index per node (dead nodes show an error)
#   kill N  kill -9 node N (simulates a crash)
#   up N    restart node N on its existing data dir
#   stop    kill every node
#   clean   stop, then delete all data and logs
set -uo pipefail

LAB="$(cd "$(dirname "$0")" && pwd)"
DATA="$LAB/etcd-data"
CLUSTER="n1=http://127.0.0.1:12380,n2=http://127.0.0.1:22380,n3=http://127.0.0.1:32380"
export ENDPOINTS="127.0.0.1:2379,127.0.0.1:22379,127.0.0.1:32379"
export ETCDCTL_API=3

client_port() { case "$1" in 1) echo 2379;; 2) echo 22379;; 3) echo 32379;; *) echo "node must be 1, 2 or 3" >&2; exit 1;; esac; }
peer_port()   { case "$1" in 1) echo 12380;; 2) echo 22380;; 3) echo 32380;; esac; }

up() {
  local n="$1" c p
  c="$(client_port "$n")"; p="$(peer_port "$n")"
  mkdir -p "$DATA"
  # The --initial-* flags are ignored when the data dir already exists, so the same command restarts a node.
  nohup etcd --name "n$n" --data-dir "$DATA/n$n" \
    --listen-client-urls "http://127.0.0.1:$c" --advertise-client-urls "http://127.0.0.1:$c" \
    --listen-peer-urls "http://127.0.0.1:$p" --initial-advertise-peer-urls "http://127.0.0.1:$p" \
    --initial-cluster "$CLUSTER" --initial-cluster-token w7lab --initial-cluster-state new \
    >>"$DATA/n$n.log" 2>&1 &
  echo $! >"$DATA/n$n.pid"
  echo "n$n started (pid $!, client :$c, log $DATA/n$n.log)"
}

kill_node() {
  local f="$DATA/n$1.pid"
  [[ -f "$f" ]] || { echo "n$1 has no pid file"; return; }
  kill -9 "$(cat "$f")" 2>/dev/null && echo "n$1 killed" || echo "n$1 was not running"
  rm -f "$f"
}

case "${1:-}" in
  start)  for n in 1 2 3; do up "$n"; done; sleep 2; "$0" status ;;
  up)     up "${2:?node number}" ;;
  kill)   kill_node "${2:?node number}" ;;
  status) etcdctl --endpoints="$ENDPOINTS" --command-timeout=2s endpoint status -w table ;;
  stop)   for n in 1 2 3; do kill_node "$n"; done ;;
  clean)  "$0" stop; rm -rf "$DATA"; echo "data removed" ;;
  *)      sed -n 3,9p "$0"; exit 1 ;;
esac
