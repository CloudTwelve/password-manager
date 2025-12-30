#!/usr/bin/env python3

import json
from pycryptodome import Crypto
import getpass

# THIS! IS! SUPER! INSECURE!
# all a hacker would need to do is delete the file, create a new password,
# and they have access to the password manager

def generate_hash(text,salt):
    text_salt = text + salt
    h = Crypto.Hash.SHA256.new()
    h.update(text_salt.encode())
    return h.hexdigest()

def startup():
    while True:
        try:
            password_hash = ""
            with open("data/master_hash.txt") as f:
                password_hash = f.read()
            password = getpass.getpass("Enter password:")
            if generate_hash(password, "hack_club_{{847c0c5265687ca799f8}}") != password_hash:
                print("Password invalid. Try again!")
                continue
            else:
                break
        except FileNotFoundError:
            print("Hey! It looks like this is your first time using the Password Manager.")
            print("You'll need to create a password.")
            password = getpass.getpass("Password: ")
            with open("data/master_hash.txt", "x") as f:
                f.write(generate_hash(password, "hack_club_{{847c0c5265687ca799f8}}"))
            continue

def change_app_pass():
    print("change app pass")

def add_pass():
    print("add_pass")

def add_pass_custom():
    print("add_pass")

def change_pass():
    print("change pass")

def change_pass_custom():
    print("change pass")

def how_many():
    num = 0
    with open("data/passwords.json") as f:
        file_cont = f.read()
        pass_dict = json.loads(file_cont)
        num = len(pass_dict)
    return num

def parse_input(input):
    if input == "help":
        command_list = """ -- help: outputs a list of possible commands (hint: it's what you just typed, :D)
        -- change-app-pass: changes master password
        -- add-pass: saves a password for a service
        -- change-pass: changes a password for a service
        -- howmany: outputs the number of passwords saved
        -- smile: outputs a smile :)"""
    elif input == "change_app_pass":
        change_app_pass()
    elif input == "add-pass":
        add_pass()
    elif input == "change_pass":
        change_pass()
    elif input == "howmany":
        how_many()
    elif input == "smile":
        print(":)")
    else:
        print("Command not recognized. Try \"help\"?")

def cmdloop():
    intro_message = "Welcome to the Password Manager! \nType \"help\" to see a list of possible commands."
    print(intro_message)

    while True:
        input= input(">> ")
        parse_input(input)


if __name__ == "__main__":
    startup()
    cmdloop()
