#!/bin/sh
# Simulates the junk that lives in real repos: 200 MB of test fixtures.
set -e
mkdir -p testdata
dd if=/dev/urandom of=testdata/fixture.bin bs=1048576 count=200 2>/dev/null
ls -lh testdata/fixture.bin
