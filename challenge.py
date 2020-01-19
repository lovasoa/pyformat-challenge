#!/usr/bin/env python3
import secrets
import sys

SECRET = secrets.token_hex()

class Sandbox:

    def ask_age(self):
        self.age = input("How old are you ? ")
        self.width = input("How wide do you want the nice box to be ? ")

    def ask_secret(self):
        if input("What is the secret ? ") == SECRET:
            print("You found the secret ! I thought this was impossible.")
            sys.exit(0)
        else:
            print("Wrong secret")

    def run(self):
        for _ in range(100):
            self.ask_age()
            to_format = f"""
Printing a {self.width}-character wide box:
[Age: {{self.age:{self.width}}} ]"""
            print(to_format.format(self=self))
            self.ask_secret()
        sys.exit(1)

Sandbox().run()
