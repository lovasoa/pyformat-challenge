#!/usr/bin/env python3
import secrets

SECRET = secrets.token_hex(64)

class Sandbox:

    def ask_age(self):
        self.age = input("How old are you ? ")
        self.width = input("How wide do you want the nice box to be ? ")

    def ask_secret(self):
        if input("What is the secret ? ") == SECRET:
            print("You found the secret ! I thought this was impossible.")
        else:
            print("Wrong secret")

    def run(self):
        while True:
            self.ask_age()
            to_format = f"""
Printing a {self.width}-character wide box:
[Age: {{self.age:{self.width}}} ]"""
            print(to_format.format(self=self))
            self.ask_secret()

Sandbox().run()
