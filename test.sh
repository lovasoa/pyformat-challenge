mkfifo fifo
python3 crack.py < fifo | python3 challenge.py | tee fifo | grep "You found the secret"