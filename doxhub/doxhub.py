#! /usr/bin/env python3

"""
DoxHub: Identify tools to find personal information.

This module contains a list of tools and sites to find personal
information about a target person.
"""

from utils.version import get_version
from utils.github_version_checker import get_latest_version
from result import QueryResult
import os
import platform
import sys
import shutil

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
    """
    Display information about the DoxHub module.

    :return:    None
    """
    print(f"""DoxHub Module

This module contains a list of tools and sites to find personal
information about a target person.""")


def center_text(text):
    """
    Center the provided text in the terminal.

    :param text:    Text to be centered
    :return:        None
    """
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
            self.prompt = input("\n\033[34m┌──(KDUser12@DoxHub)-[~]\n└─$ \033[0m")
            self.get_command()

    def get_command(self):
        if not self.find_command():
            return

        if self.prompt == 13:
            about_command()
        elif self.prompt == 14:
            exit(0)
        else:
            QueryResult(self.prompt, commands[self.prompt])

    def find_command(self):
        try:
            self.prompt = int(self.prompt)
            if self.prompt in commands:
                return True
            else:
                print("\033[31m[\033[0m!\033[31m]\033[0m Please enter a valid value.")
                return False
        except ValueError:
            print("\033[31m[\033[0m!\033[31m]\033[0m Please enter a valid value.")
            return False

def clear_output():
    """
    Clear the terminal screen.

    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    version = get_version((1,0,0,'final', 0))
    latest_version_message = get_latest_version("DoxHub", f"v{version}")
    clear_output()

    if latest_version_message:
        print(latest_version_message)
        # return

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
