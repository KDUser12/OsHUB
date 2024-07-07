"""
DoxHub: Identify tools to find personal information.

This module contains a list of tools and sites to find personal
information about a target person.
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter

# Removing __version__ here will trigger update message for users.
# Do not remove until ready to trigger that message.
# When removed, also remove all the noqa: E402 comments for linting.
__version__ = "2.0b0"
del __version__

from __init__ import (  # noqa: E402
    __longname__,
    __version__
)


def main():
    parser = ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        description="{} (Version {})".format(__longname__, __version__),
        epilog="test"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="DoxHub v{}".format(__version__),
        help="Display version information and dependencies."
    )

    args = parser.parse_args()
