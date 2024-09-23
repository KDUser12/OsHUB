#!/usr/bin/env python3

"""
OsHUB

OsHUB is a program referencing several tools and websites to make
Osint for legal purposes.

~~~~~~~~~~~~~~~~~~~~~
Source: https://github.com/KDUser12/OsHUB
(c) 2024 KDUser12
Released under the Apache License 2.0
"""

import socket
import os

from colorama import Fore, Style

from __init__ import __version__, forge_api_latest_release
from core.management.manager import commands

from utils.alignment import center, alignment
from utils.update import check_versions


def clear_output():
    command = 'cls' if os.name == 'nt' else 'clear'
    return os.system(command)


class OsHUB:
    def __init__(self) -> None:
        self.current_version = __version__
        self.latest_version = check_versions

        self.device_name = socket.gethostname()
        self.user_name = os.getlogin()
        self.directory = os.path.abspath("")

        clear_output()

        center(f"""{Fore.BLUE}
                
                
 ██████╗ ███████╗██╗  ██╗██╗   ██╗██████╗ 
██╔═══██╗██╔════╝██║  ██║██║   ██║██╔══██╗
██║   ██║███████╗███████║██║   ██║██████╔╝
██║   ██║╚════██║██╔══██║██║   ██║██╔══██╗
╚██████╔╝███████║██║  ██║╚██████╔╝██████╔╝
 ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
        """)
        alignment(f"> [TM] Made by KDUser12\n> [?] {self.current_version} Changelog", f"About [:] <\nExit [!] <")
        print(Fore.RESET + "\n")

        for x in range(1, 10):
            message = f"{Fore.BLUE}({Fore.RESET}0{x}{Fore.BLUE}){Fore.RESET} > {commands[str(x)]}"
            if str(x + 9) in commands:
                space = " " * (50 - len(message))
                message += f"{space}{Fore.BLUE}({Fore.RESET}{x + 9}{Fore.BLUE}){Fore.RESET} > {commands[str(x + 9)]}"
            print(message)

        if self.latest_version:
            print(f"\nInstall the latest OsHUB for new features and improvements! https://github.com/kduser12/oshub/releases/latest")
