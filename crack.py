#!/usr/bin/env python3

password = ""
answer = ""

while not "You found the secret" in answer:
    print(0)
    print("HACK_EVERYTHING") # TODO: find how to hack everything
    input()
    input()
    password += extract_password_char(input()) # TODO: find how to extract a password character
    print(password)
    answer = input()
