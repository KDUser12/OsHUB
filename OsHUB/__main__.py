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

from utils._os import check_os_compatibility
from utils.env import check_python_version


if __name__ == '__main__':
    required_versions = ['3.6', '3.7', '3.8']
    
    try:
        check_os_compatibility()
        check_python_version(required_versions)
    except EnvironmentError as error:
        exit(f"Error: {error}")

    import oshub
    oshub.main()
