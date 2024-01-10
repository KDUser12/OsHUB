#! /usr/bin/env python3

"""
DoxHub: Identify tools to find personal information.

This module contains a list of tools and sites to find personal
information about a target person.
"""

import sys


if __name__ == '__main__':
    try:
        # Check if the user is using the correct version of Python.
        python_version = sys.version.split()[0]

        if sys.version_info < (3, 8):
            print("DoxHub requires Python 3.8+\nYou are using Python %s, which is not supported by DoxHub" % (
                python_version))
            exit(1)

        import doxhub
        doxhub.main()
    except Exception as error:
        print(f"\033[31m[\033[0m!\033[31m]\033[0m Error : {error}")
        exit(1)

