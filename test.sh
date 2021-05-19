#!/usr/bin/env bash

set -o pipefail

rm -f fifo
mkfifo fifo
./crack.py < fifo | ./challenge.py | tee fifo
rm -f fifo
