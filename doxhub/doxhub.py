#! /usr/bin/env python3

"""
DoxHub: Identify tools to find personal information.

This module contains a list of tools and sites to find personal
information about a target person.
"""

from utils.version import get_version
import os
import platform
import sys
import shutil
from result import QueryResult

commands = {
    1: 'Username',
    2: 'Email Address',
    3: 'IP Address',
    4: 'Telephone Numbers',
    5: 'Exploits',
    6: 'Archives',
    7: 'Dark Web',
    8: 'Transportation',
    9: 'Data Leaks',
    10: 'Phishing',
    11: 'Gore',
    12: 'Other',
    13: 'About',
    14: 'Exit'
}


def about_command():
    print(f"""DoxHub Module v{get_version((1,0,0,'final', 0))}

This module contains a list of tools and sites to find personal
information about a target person.""")


def center_text(text):
    lines = text.split('\n')
    terminal_width, _ = shutil.get_terminal_size()

    for line in lines:
        padding = (terminal_width - len(line)) // 2
        print(" " * padding + line)

class Commands:
    def __init__(self):
        self.prompt = None

        self.call_command()

    def call_command(self):
        while True:
            self.prompt = input("\n\033[34m┌──(KDUser@DoxHub)-[~]\n└─$ \033[0m")
            self.get_command()

    def get_command(self):
        if not self.find_command():
            return

        if self.prompt == 13:
            about_command()
        elif self.prompt == 14:
            sys.exit(0)
        else:
            QueryResult(self.prompt, commands[self.prompt])

    def find_command(self):
        try:
            self.prompt = int(self.prompt)
            if self.prompt in commands or self.prompt == 0:
                return True
            else:
                print("\033[31m[\033[0m!\033[31m]\033[0m Please enter a valid value.")
                return False
        except ValueError:
            print("\033[31m[\033[0m!\033[31m]\033[0m Please enter a valid value.")
            return False

def clear_output():
    os.system('cls' if platform == 'Windows' else 'clear')


def main():
    version = get_version((0,1,0,'beta', 0))
    clear_output()
    center_text(f"""\033[34m
██████╗  ██████╗ ██╗  ██╗██╗  ██╗██╗   ██╗██████╗ 
██╔══██╗██╔═══██╗╚██╗██╔╝██║  ██║██║   ██║██╔══██╗
██║  ██║██║   ██║ ╚███╔╝ ███████║██║   ██║██████╔╝
██║  ██║██║   ██║ ██╔██╗ ██╔══██║██║   ██║██╔══██╗
██████╔╝╚██████╔╝██╔╝ ██╗██║  ██║╚██████╔╝██████╔╝
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝
\033[0m""")

    print(f"\033[34m[M] Made by KDUser\n[?] {version} Changelog\033[0m\n\n")

    for i in range(1, 10):
        action = f"\033[34m(\033[0m0{i}\033[34m)\033[0m > {commands[i]}"
        if i + 9 in commands:
            space = ""
            number = 50 - len(action)
            for a in range(1, number):
                space += " "
            action += f"{space}\033[34m(\033[0m{i + 9}\033[34m)\033[0m > {commands[i + 9]}"
        print(action)

    Commands()
