"""
DoxHub: Identify tools to find personal information.

This module contains a list of tools and sites to find personal
information about a target person.
"""

import sys

if __name__ == '__main__':
    # Check if the user is using the correct version of Python.
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 8):
        exit("DoxHub requires Python 3.8+ You are using Python {}, which is not supported by DoxHub".format(python_version))

    import doxhub
    doxhub.main()
