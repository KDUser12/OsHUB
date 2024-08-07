#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DoxHub

This Module contains a list of tools and sites to find personal
information about a target person.

~~~~~~~~~~~~~~~~~~~~~
Source: https://github.com/KDUser12/DoxHub
(c) 2024 KDUser12
Released under the MIT License
"""

import os
from colorama import Fore, Style
import shutil
import socket

from __init__ import __version__
from utils.update import check_versions
from result import QueryResult


def about_command():
    """about_command - Display information about the DoxHub Module.
    
    Extended Summary:
    This function prints out a brief description of the DoxHub module. 
    DoxHub contains a list of tools and sites designed to help find personal 
    information about a target person. It is intended to provide users with 
    information on the purpose and usage of the module.
    """
    
    print("""DoxHub module.
DoxHub contains a list of tools and sites to find personal
information about a target person.""")


def changelog_command():
    """changelog_command - Display the changelog for the DoxHub Module.
    
    Extended Summary:
    This function prints the patch notes for the DoxHub module. It includes 
    information about new features, bug fixes, changes, and removed features 
    for version 3.0 as of 08-08-2024. The changelog is formatted to highlight 
    various sections such as new features, bug fixes, changes, and removals.
    """
    
    print(f"""{Style.BRIGHT}Patch Notes - DoxHub{Style.NORMAL}
{Style.BRIGHT}Version 3.0 - 08-08-2024{Style.NORMAL}
{Style.DIM}New Features{Style.NORMAL}
- Checking operating system compatibility.
- Adding a gitignore library.

{Style.DIM}Bug Fixes{Style.NORMAL}
- Fix - Fixed - Fixed display of `True` message when calling a command.

{Style.DIM}Changes{Style.NORMAL}
- File name `PATCHNOTE.md` replaced in `PATCH_NOTES.md`.
- New Patch Notes display format.
- New program version management.
- New comment display format.
- New Python version compatibility management.
- Changed update management.
- Changed the display of the update message.
- Changelog update.

{Style.DIM}Removed{Style.NORMAL}
- Removed the letter `v` when naming the current version of the program.
- Removing the `TM` command.""")


commands = {
    1: "Username",
    2: "Email Address",
    3: "IP Address",
    4: "Telephone Numbers",
    5: "Exploits",
    6: "Archives",
    7: "Dark Web",
    8: "Transportation",
    9: "Data Leaks",
    10: "Phishing",
    11: "DDoS"
}


special_commands = {
    ":": about_command,
    "!": exit,
    "?": changelog_command
}


class DoxHub:
    def __init__(self):
        """Management of user-entered commands from a command line interface.
        """

        self.device_name = socket.gethostname()
        self.user_name = os.getlogin()
        self.directory = os.path.abspath("")
        self.prompt = ""

        self.call_command()

    def call_command(self):
        """Calling a command from a prompt.
        """

        try:
            while True:
                self.prompt = input(f"\n{Fore.BLUE}┌──({self.user_name}@{self.device_name})-[{self.directory}]\n└─$ {Fore.RESET}")
                self.get_command()
        except KeyboardInterrupt:
            exit("\n")

    def get_command(self):
        if self.find_command():
            if isinstance(self.prompt, str):
                return special_commands[self.prompt]()
            return QueryResult(self.prompt, commands[self.prompt])
    
    def find_command(self) -> bool:
        """Search for the command entered by the user.

        Returns:
            bool: command search result
        """

        if self.prompt not in special_commands:
            try:
                self.prompt = int(self.prompt)
            except ValueError:
                print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Please enter a valid value.")
                return False

        if self.prompt in commands or self.prompt in special_commands:
            return True

        print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Please enter a valid command.")


def center_text(text: str):
    """Center the provided text in the terminal.

    Args:
        text (str): Text to be centered
    """

    lines = text.split('\n')
    terminal_width, _ = shutil.get_terminal_size()

    for line in lines:
        padding = (terminal_width - len(line)) // 2
        print(" " * padding + line)


def right_text(left_text: str, right_text: str):
    """Right and left movement of text provided.

    Args:
        left_text (str): Text to move left
        right_text (str): Text to move right
    """

    left_lines = left_text.split('\n')
    right_lines = right_text.split('\n')
    terminal_width, _ = shutil.get_terminal_size()

    for index, left_line in enumerate(left_lines):
        padding = (terminal_width - len(right_lines[index]) - len(left_line))
        print(f"{left_line}" + " " * padding + right_lines[index])


def clear_output():
    """Clear the terminal screen.

    Returns:
        int: StrOrBytesPath
    """

    command = 'cls' if os.name == 'nt' else 'clear'
    return os.system(command)


def main():
    current_version = f"{__version__}"
    latest_version = check_versions("doxhub", current_version)
    clear_output()
    
    center_text(f"""{Fore.BLUE}
██████╗  ██████╗ ██╗  ██╗██╗  ██╗██╗   ██╗██████╗ 
██╔══██╗██╔═══██╗╚██╗██╔╝██║  ██║██║   ██║██╔══██╗
██║  ██║██║   ██║ ╚███╔╝ ███████║██║   ██║██████╔╝
██║  ██║██║   ██║ ██╔██╗ ██╔══██║██║   ██║██╔══██╗
██████╔╝╚██████╔╝██╔╝ ██╗██║  ██║╚██████╔╝██████╔╝
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
""")
    
    right_text(f"> [TM] Made by KDUser12\n> [?] {current_version} Changelog", f"About [:] <\nExit [!] <")
    print(f"\n{Fore.RESET}")

    for count in range(1, 10):
        message = f"{Fore.BLUE}({Fore.RESET}0{count}{Fore.BLUE}){Fore.RESET} > {commands[count]}"
        
        if count + 9 in commands:
            space = " " * (50 - len(message))
            message = message + f"{space}{Fore.BLUE}({Fore.RESET}{count + 9}{Fore.BLUE}){Fore.RESET} > {commands[count + 9]}"
        print(message)
        
    if latest_version:
        print("\nInstall the latest DoxHub for new features and improvements! https://github.com/KDUser12/DoxHub/releases/latest")

    DoxHub()
