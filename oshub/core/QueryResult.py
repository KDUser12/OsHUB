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

from colorama import Fore

from resources.tools import tools
from resources.websites import websites


def check_value(dictionary) -> bool:
    if isinstance(dictionary, dict):
        return any(bool(inner) for inner in dictionary.values())
    elif isinstance(dictionary, set):
        return bool(dictionary)
    return False


class QueryResult:
    def __init__(self, command, option) -> None:
        self.command = command
        self.option = option

        print(self.format_output())

    def format_output(self) -> str:
        formatted_output = ""
        if check_value(tools[self.command]):
            formatted_output = formatted_output + (f"\n{Fore.BLUE}[{Fore.RESET}*{Fore.BLUE}]{Fore.RESET} {self.option} "
                                                  f"- Tools :")
            for tool in tools[self.command]:
                formatted_output = formatted_output + f"\n- {tool}"

        if check_value(websites[self.command]):
            if check_value(tools[self.command]):
                formatted_output = formatted_output + "\n"

            formatted_output = formatted_output + (f"\n{Fore.BLUE}[{Fore.RESET}*{Fore.BLUE}]{Fore.RESET} {self.option} "
                                                  f"- Websites :")
            for website in websites[self.command]:
                formatted_output = formatted_output + f"\n- {website}"
        return formatted_output

    def __str__(self):
        return f"QueryResult(command={self.command}, option={self.option})"
