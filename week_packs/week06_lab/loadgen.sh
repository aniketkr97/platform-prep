#!/usr/bin/env bash
# About 20 requests/second against the toy service until Ctrl-C.
while true; do
  for _ in 1 2 3 4 5 6 7 8 9 10; do
    curl -s -o /dev/null localhost:8000/work &
  done
  wait
  sleep 0.5
done
