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
- Changing the display of the prompt.
- Changing the docstring.
- Changed the introductory display.

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
    """DoxHub - Management of user-entered commands from a command line interface.

    Extended Summary:
    The `DoxHub` class is designed to handle the command-line interface for the DoxHub tool. 
    It manages user interactions, processes commands, and provides a prompt similar to a 
    terminal shell. Upon initialization, it gathers system information, such as the device name 
    and username, and starts the command input loop.

    Attributes:
        device_name (str): The hostname of the device.
        user_name (str): The username of the current logged-in user.
        directory (str): The current working directory.
        prompt (str): The command prompt string displayed to the user.

    Methods:
        call_command: Continuously prompt the user for commands and execute them.
        get_command: Determine and execute the appropriate command based on user input.
        find_command: Check if the entered command is valid.
    """
    
    def __init__(self):
        """__init__ - Initialize the DoxHub class.

        Extended Summary:
        This constructor initializes the `DoxHub` object by setting up essential attributes 
        like `device_name`, `user_name`, and `directory`. It then calls the `call_command` 
        method to begin processing user commands from the command-line interface.
        """

        self.device_name = socket.gethostname()
        self.user_name = os.getlogin()
        self.directory = os.path.abspath("")
        self.prompt = ""

        self.call_command()

    def call_command(self):
        """call_command - Start the command input loop.

        Extended Summary:
        This method continuously prompts the user to enter a command. It constructs the command prompt 
        using the system's username, device name, and current directory. The input is then processed by 
        the `get_command` method. The loop runs until the user interrupts it with a keyboard signal (Ctrl+C).
        """

        try:
            while True:
                self.prompt = input(f"\n┌──({Fore.BLUE}{Style.BRIGHT}{self.user_name}@{self.device_name}{Style.RESET_ALL}"
                                    f"{Fore.RESET})-[{Fore.BLUE}{Style.BRIGHT}{self.directory}{Style.RESET_ALL}{Fore.RESET}]"
                                    f"\n└─{Fore.BLUE}{Style.BRIGHT}$ {Style.RESET_ALL}{Fore.RESET}")
                self.get_command()
        except KeyboardInterrupt:
            exit("\n")

    def get_command(self):
        """get_command  Process and execute the user's command.

        Extended Summary:
        This method checks if the command entered by the user is valid using the `find_command` method.
        If valid, it either executes a special command or returns a query result based on the command type.

        Returns:
            None -- Executes the command or returns a result based on the input.
        """
        if self.find_command():
            if isinstance(self.prompt, str):
                return special_commands[self.prompt]()
            return QueryResult(self.prompt, commands[self.prompt])
    
    def find_command(self) -> bool:
        """find_command Search for the command entered by the user.

        Extended Summary:
        This method determines whether the command entered by the user is valid by checking 
        against predefined commands and special commands. It also handles user input errors 
        by prompting for valid input if necessary.

        Returns:
            bool -- True if the command is found; False otherwise.
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
        return False


def center_text(text: str):
    """center_text - Center the provided text in the terminal.

    Extended Summary:
    This function takes a multi-line string as input and centers each line
    within the current terminal width. It calculates the necessary padding
    for each line to be centrally aligned and prints it accordingly.

    Arguments:
        text {str} -- The text to be centered, which can span multiple lines.
    """

    lines = text.split('\n')
    terminal_width, _ = shutil.get_terminal_size()

    for line in lines:
        padding = (terminal_width - len(line)) // 2
        print(" " * padding + line)


def right_text(left_text: str, right_text: str):
    """right_text - Align left and right text within the terminal.

    Extended Summary:
    This function prints two strings on the same line in the terminal, 
    one aligned to the left and the other to the right. It splits the input 
    strings into lines and calculates the necessary padding between the 
    left and right text to ensure proper alignment within the terminal width.

    Arguments:
        left_text {str} -- The text to be aligned on the left.
        right_text {str} -- The text to be aligned on the right.
    """

    left_lines = left_text.split('\n')
    right_lines = right_text.split('\n')
    terminal_width, _ = shutil.get_terminal_size()

    for index, left_line in enumerate(left_lines):
        padding = (terminal_width - len(right_lines[index]) - len(left_line))
        print(f"{left_line}" + " " * padding + right_lines[index])


def clear_output():
    """clear_output - Clear the terminal screen.

    Extended Summary:
    This function clears the terminal screen by executing the appropriate 
    system command based on the operating system (e.g., 'cls' for Windows and 
    'clear' for Unix-like systems). It is useful for resetting the terminal view.

    Returns:
        int -- The return code from the system command, indicating success or failure.
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
