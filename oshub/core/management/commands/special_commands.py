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

from __init__ import __longname__, __version__

def about_command():
    print(f"{__longname__} (Version {__version__})\n"
          f"OsHUB is a program referencing several tools and websites to make\n"
          f"Osint for legal purposes.")

def changelog_command():
    print("""# **ChangeLog - OsHUB**
## **Version 4.0 - 09-23-2024**
### *New Features*
- Adding a log system.
- Added several commands (`python3 oshub -h`) when calling the module.
prise
- Checking and installing packages when launching the program.
- Added a file listing all commands.
- Extracting the kernel version for "os_version" for any Linux distribution. (especially for Arch Linux)
- Added the `archive it` site and `archive blog` in the “archive” category.

### *Changes*
- New version system.
- Moved text organization functions to `utils/alignment.py`.
- Reorganization of classes and basic functions.
- Changed the repository recovery method.
- Reorganization of classes and functions management commands.
- File name `sites.py` replaced in `websites.py`.
- Changed the `Dark Web` category to `Browser`.

### *Bug Fixes*
- Fix - Fixed - File name `CHANGELOGS.md` replaced in `CHANGELOG.md`.
- Fix - Remove - Site `https://checkusernames.com` that brings connection problems.
- Fix - Remove - Site `https://numberingplans.com` is broken.
- Fix - Remove - Site `https://breachforums.is` (oops).

### *Internal change*
- Changed VSCode text editor to PyCharm Community Edition from JetBrain.
- Change of project license to `Apache License 2.0`.""")

def exit_command():
    exit("Exiting OsHUB...")
