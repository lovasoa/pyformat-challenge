#!/usr/bin/env bash

set -o pipefail

mkfifo fifo
./crack.py < fifo | ./challenge.py | tee fifo
rm -f fifo
