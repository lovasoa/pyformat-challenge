#!/usr/bin/env python3

password = ""
answer = ""

while not "You found the secret" in answer:
    print(0)
    print("{self.ask_secret.__globals__[SECRET][%d]}>9" % (i,))
    input()
    input()
    password += input()[10]
    print(password)
    answer = input()
