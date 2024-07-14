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


def about_command():
    """Display information about the DoxHub Module.
    """

    print("""DoxHub module.
DoxHub contains a list of tools and sites to find personal
information about a target person.""")


def tm_command():
    """Display information about the creation of DoxHub.
    """

    print("""DoxHub is a program created by KDUser12 on GitHub on January 5, 2024""")


def changelog_command():
    print(f"""CHANGELOG v{__version__}
    
News:
- Ignoring `.pyc` files.
- Added a file containing information about new versions, Beta only.
- Version plugin change.
- Compatibility with new versions of Python (3.13).
- Addition of a `requirements.txt` file allowing you to know and install the necessary modules.
- The `github_version_checker.py` file was renamed to `update.py`.
- Possible error handling in the `update.py` file.
- Using `colorama` to manage colors.
- Changing the menu display format.
- Changed the display of the prompt.
    - Display username.
    - Display of device name.
    - Displaying the program execution directory.
- Invalid commands management.
- Modification of the `ressources` folder, renamed to `resources`.
- Checking the existence of a value in a dictionary to avoid an empty display.
- Updated the results display format.
- Updating the `README.md` file.
- Updating security policy.
- Ignoring `.idea/` folder.
- Added specific commands.
  - `!`: Exit command.
  - `:`: About command.
  - `?`: Changelog command.
- Ignoring `venv/` folder.

Deleted:
- Removed - Directory `.github/`.
- Removed - Python versions previous to 3.8.x.
- Removed - List of sites and tools considered too violent.

Bugs:
- Fix - Handling the `KeyboardInterrupt` error.
- Fix - Fixed command naming offset.
""")


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
    "TM": tm_command,
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
            print(isinstance(self.prompt, int))
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
    
    right_text(f"> [TM] Made by KDUser12\n> [?] {current_version} Changelog", f"About [:] <\nExit [!] <")
    print(f"\n{Fore.RESET}")

    for count in range(1, 10):
        message = f"{Fore.BLUE}({Fore.RESET}0{count}{Fore.BLUE}){Fore.RESET} > {commands[count]}"
        
        if count + 9 in commands:
            space = " " * (50 - len(message))
            message = message + f"{space}{Fore.BLUE}({Fore.RESET}{count + 9}{Fore.BLUE}){Fore.RESET} > {commands[count + 9]}"
        print(message)

    DoxHub()
