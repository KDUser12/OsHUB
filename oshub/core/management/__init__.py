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

from core.management.manager import commands, special_commands
from core.QueryResult import QueryResult

class CommandHandler:
    def __init__(self) -> None:
        self.commands = commands
        self.special_commands = special_commands

    def is_valid_command(self, command) -> bool:
        return command in self.commands or command in self.special_commands

    def execut_command(self, command):
        if command in self.special_commands:
            return self.special_commands[command]()
        return QueryResult(command, self.commands[command])
