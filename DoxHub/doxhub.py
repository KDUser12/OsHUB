""" DoxHub: Identify tools to find personal information.

This module contains a list of tools and sites to find personal
information about a target person.
"""

import os
from colorama import Fore
import shutil
import socket

from __init__ import __version__
from utils.update import get_latest_version
from result import QueryResult

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
            QueryResult(self.prompt, commands[self.prompt])
    
    def find_command(self):
        """Search for the command entered by the user.

        Returns:
            bool: command search result
        """

        try:
            self.prompt = int(self.prompt)
            if self.prompt in commands:
                return True
            print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Please enter a valid command.")
        except ValueError:
            print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Please enter a valid value.")
        return False


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
    current_version = f"v{__version__}"
    latest_version = get_latest_version(current_version)
    clear_output()

    if latest_version:
        print(Fore.RED + latest_version + Fore.RESET)
    
    center_text(f"""{Fore.BLUE}
██████╗  ██████╗ ██╗  ██╗██╗  ██╗██╗   ██╗██████╗ 
██╔══██╗██╔═══██╗╚██╗██╔╝██║  ██║██║   ██║██╔══██╗
██║  ██║██║   ██║ ╚███╔╝ ███████║██║   ██║██████╔╝
██║  ██║██║   ██║ ██╔██╗ ██╔══██║██║   ██║██╔══██╗
██████╔╝╚██████╔╝██╔╝ ██╗██║  ██║╚██████╔╝██████╔╝
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
""")
    
    right_text(f"> [TM] Made by KDUser12\n> [?] {current_version} Changelog", f"About [!] <\nExit [~] <")
    print(f"\n{Fore.RESET}")

    for count in range(1, 10):
        message = f"{Fore.BLUE}({Fore.RESET}0{count}{Fore.BLUE}){Fore.RESET} > {commands[count]}"
        
        if count + 9 in commands:
            space = " " * (50 - len(message))
            message = message + f"{space}{Fore.BLUE}({Fore.RESET}{count + 9}{Fore.BLUE}){Fore.RESET} > {commands[count + 9]}"
        print(message)

    DoxHub()
