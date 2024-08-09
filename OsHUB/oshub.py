#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
OsHUB

This Module contains a list of tools and sites to find personal
information about a target person.

~~~~~~~~~~~~~~~~~~~~~
Source: https://github.com/KDUser12/OsHUB
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
    """about_command - Display information about the OsHUB Module.
    
    Extended Summary:
    This function prints out a brief description of the OsHUB module. 
    OsHUB contains a list of tools and sites designed to help find personal 
    information about a target person. It is intended to provide users with 
    information on the purpose and usage of the module.
    """
    
    print("""OsHUB module.
OsHUB contains a list of tools and sites to find personal
information about a target person.""")


def changelog_command():
    """changelog_command - Display the changelog for the OsHUB Module.
    
    Extended Summary:
    This function prints the patch notes for the OsHUB module. It includes 
    information about new features, bug fixes, changes, and removed features 
    for version 3.0 as of 08-08-2024. The changelog is formatted to highlight 
    various sections such as new features, bug fixes, changes, and removals.
    """
    
    print(f"""{Style.BRIGHT}Patch Notes - OsHUB{Style.NORMAL}
{Style.BRIGHT}Version 3.1 - 08-09-2024{Style.NORMAL}
{Style.DIM}Changes{Style.NORMAL}
- The Source File was renamed to `OsHUB`.
- Change of name `DoxHub` to `OsHUB` in changelogs.
- Change of name `DoxHub` to `OsHUB` in `README.md`
- `PATCH_NOTES.md` file renamed to `CHANGELOGS.md`
- Changed name from `DoxHub` to `OsHUB` throughout source code.
- `doxhub.py` file renamed to `oshub.py`
- Change of title.
- Changing the screenshot.
- Update changelogs

{Style.BRIGHT}Version 3.0 - 08-08-2024{Style.NORMAL}
{Style.DIM}New Features{Style.NORMAL}
- Checking operating system compatibility.
- Adding a gitignore library.
- New command management.
- Added search engines.
- Added image/face search engines.
- Added data viewer.
- Added new sites/tools for usernames.
- Added `Social Network` for advanced searches on social networks.
- Added geolocation.
- Adding a new data leak site.

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
    "1": "Username",
    "2": "Email Address",
    "3": "IP Address",
    "4": "Telephone Numbers",
    "5": "Exploits",
    "6": "Archives",
    "7": "Dark Web",
    "8": "Transportation",
    "9": "Data Leaks",
    "10": "Phishing",
    "11": "DDoS",
    "12": "Search Engine",
    "13": "Face/Image Search Engine",
    "14": "Data Viewer",
    "15": "Social Network",
    "16": "Geolocation"
}

special_commands = {
    ":": about_command,
    "!": exit,
    "?": changelog_command
}


class CommandHandler:
    """ CommandHandler - Handles the execution and validation of commands.

    Extended Summary:
    The `CommandHandler` class is responsible for managing and executing commands provided by the user. 
    It contains methods to check if a command is valid and to execute commands from either a standard 
    command set or special commands.

    Attributes:
        commands (dict): A dictionary of standard commands and their corresponding functions.
        special_commands (dict): A dictionary of special commands and their corresponding functions.

    Methods:
        is_valid_command: Check if the command is valid.
        execute_command: Execute the provided command.
    """
    
    def __init__(self) -> None:
        """__init__ - Initialize the CommandHandler class.

        Extended Summary:
        This constructor initializes the `CommandHandler` with predefined commands and special commands.
        """
        
        self.commands = commands
        self.special_commands = special_commands
        
    def is_valid_command(self, command) -> bool:
        """is_valid_command - Check if the command is valid.

        Extended Summary:
        This method verifies whether the provided command exists in either the standard command list or 
        the special commands list.

        Arguments:
            command {str} -- The command string to validate.

        Returns:
            bool -- True if the command is valid, False otherwise.
        """
        
        return command in self.commands or command in self.special_commands
    
    def execut_command(self, command):
        """execut_command - Execute the provided command.

        Extended Summary:
        This method executes the command by checking if it belongs to special commands or standard commands 
        and then calling the respective function.

        Arguments:
            command {str} -- The command to execute.

        Returns:
            None -- The result of the command execution or function call.
        """
        
        if command in self.special_commands:
            return self.special_commands[command]()
        return QueryResult(command, self.commands[command])


class OsHUB:
    """ OsHUB - Main class to manage the user interface and command execution.

    Extended Summary:
    The `OsHUB` class is the core of the application, responsible for managing the user interface, 
    handling the input loop, and coordinating with the `CommandHandler` to process and execute user commands.

    Attributes:
        device_name (str): The hostname of the device.
        user_name (str): The username of the current logged-in user.
        directory (str): The current working directory.
        command_handler (CommandHandler): An instance of CommandHandler to manage commands.

    Methods:
        display_prompt: Generate the command prompt string.
        run: Start the command input loop.
        process_command: Process and execute the user's command.
    """
    
    def __init__(self):
        """__init__ - Initialize the OsHUB class.

        Extended Summary:
        This constructor initializes the `OsHUB` object by setting up system-related attributes and 
        an instance of `CommandHandler` to manage user commands. It then starts the command input loop.
        """

        self.device_name = socket.gethostname()
        self.user_name = os.getlogin()
        self.directory = os.path.abspath("")
        self.command_handler = CommandHandler()

        self.run()
        
    def display_prompt(self) -> str:
        """display_prompt - Generate the command prompt string.

        Extended Summary:
        This method generates and returns a string representing the command prompt, which includes 
        the username, device name, and current directory, formatted with color codes.
        
        Returns:
            str -- The formatted command prompt string.
        """    
    
        return (f"\n┌──({Fore.BLUE}{Style.BRIGHT}{self.user_name}@{self.device_name}{Style.RESET_ALL}"
                f"{Fore.RESET})-[{Fore.BLUE}{Style.BRIGHT}{self.directory}{Style.RESET_ALL}{Fore.RESET}]"
                f"\n└─{Fore.BLUE}{Style.BRIGHT}$ {Style.RESET_ALL}{Fore.RESET}")

    def run(self):
        """run - Start the command input loop.

        Extended Summary:
        This method initiates an infinite loop, prompting the user to enter commands, which are then 
        processed and executed. The loop can be terminated by a keyboard interrupt (Ctrl+C).
        """
        
        try:
            while True:
                command = input(self.display_prompt())
                self.process_command(command)
        except KeyboardInterrupt:
            print("\nExiting OsHUB...")

    def process_command(self, command):
        """process_command - Process and execute the user's command.

        Extended Summary:
        This method processes the command entered by the user. It checks if the command is valid 
        using the `CommandHandler` and executes it. If the command is invalid, an error message 
        is displayed.

        Arguments:
            command {str} -- The command entered by the user.
        """
        
        if self.command_handler.is_valid_command(command):
            self.command_handler.execut_command(command)
        else:
            print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Invalid command. Please try again.")


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
    latest_version = check_versions("OsHUB", current_version)
    clear_output()
    
    center_text(f"""{Fore.BLUE}
                
                
 ██████╗ ███████╗██╗  ██╗██╗   ██╗██████╗ 
██╔═══██╗██╔════╝██║  ██║██║   ██║██╔══██╗
██║   ██║███████╗███████║██║   ██║██████╔╝
██║   ██║╚════██║██╔══██║██║   ██║██╔══██╗
╚██████╔╝███████║██║  ██║╚██████╔╝██████╔╝
 ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
""")
    
    right_text(f"> [TM] Made by KDUser12\n> [?] {current_version} Changelog", f"About [:] <\nExit [!] <")
    print(f"\n{Fore.RESET}")

    for count in range(1, 10):
        message = f"{Fore.BLUE}({Fore.RESET}0{count}{Fore.BLUE}){Fore.RESET} > {commands[str(count)]}"
        
        if str(count + 9) in commands:
            space = " " * (50 - len(message))
            message = message + f"{space}{Fore.BLUE}({Fore.RESET}{count + 9}{Fore.BLUE}){Fore.RESET} > {commands[str(count + 9)]}"
        print(message)
        
    if latest_version:
        print("\nInstall the latest OsHUB for new features and improvements! https://github.com/KDUser12/OsHUB/releases/latest")

    OsHUB()
