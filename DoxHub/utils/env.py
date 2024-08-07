#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def check_python_version(required_versions):
    """check_python_version - Verify if the current Python version meets the required versions.

    Extended Summary:
    This function checks if the current Python version satisfies any of the versions
    specified in the `required_versions` list. It compares the current version against
    each required version, logging the results and raising an EnvironmentError if
    the current version does not meet any of the required versions.

    Arguments:
        required_versions {list of str} -- A list of version strings that are required,
        e.g. ['3.6', '3.7', '3.8'].

    Raises:
        EnvironmentError: If the current Python version is less than any of the required versions
    """
    
    current_version = sys.version_info
    current_version_str = '.'.join(map(str, current_version[:3]))
    
    for version in required_versions:
        required_versions = tuple(map(int, version.split('.')))
    
        if current_version < required_versions:
            raise EnvironmentError(f"Python version required: {'.'.join(map(str, required_versions))}, "
                                   f"current version: {current_version_str}")
    