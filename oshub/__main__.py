#! /usr/bin/env python3

"""
OsHUB

OsHUB is a program referencing several tools and websites to make
Osint for legal purposes.

~~~~~~~~~~~~~~~~~~~~~
Source: https://github.com/KDUser12/OsHUB
(c) 2024 KDUser12
Released under the Apache License 2.0
"""

import logging
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from __init__ import __shortname__, __longname__, __version__

from utils._os import check_os_compatibility
from utils.env import check_python_version
from utils.packages import check_and_install_dependencies


def setup_logging(debug=False):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('logs.log', mode='a')
        ]
    )

if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter, description=f"{__longname__} (Version {__version__})")
    parser.add_argument("-v", "--version",
        action="version",
        version=f"{__shortname__} v{__version__}",
        help="display version information and dependencies")
    parser.add_argument("-d", "--debug",
        action="store_true",
        default=False,
        help="display extra debugging information and metrics")

    args = parser.parse_args()
    setup_logging(args.debug)

    required_versions = ['3.6', '3.7', '3.8']
    logging.debug(f"Required versions : {required_versions}")

    try:
        check_os_compatibility()
        check_python_version(required_versions)
    except EnvironmentError as error:
        logging.error(f"Error: {error}")
        exit(1)

    check_and_install_dependencies(['requirements.txt'])
