#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform
import subprocess
import re


def get_linux_version():
    """get_linux_version - Get a simplified version string for Linux using lsb_release.

    Extended Summary:
    This function runs the 'lsb_release -r' command to fetch the Linux distribution
    version. It parses the output to extract and return the version number. If the
    command fails, it logs an error and returns None.

    Returns:
        str -- The Linux version string if successfully retrieved, otherwise None.
    """
    
    try:
        result = subprocess.run(['lsb_release', '-r'], capture_output=True, text=True, check=True)
        # Extract the version number from the output
        version_line = result.stdout.strip().split('\n')[0]
        version = version_line.split(':')[1].strip()
    except subprocess.CalledProcessError as error:
        raise EnvironmentError(f"Failed to get Linux version: {error}")
    return version


def check_os_compatibility():
    """check_os_compatibility - Check the compatibility of the current operating system.

    Extended Summary:
    This function determins the current operating system and version, logging the
    detected OS details. It then verifies whether the OS is supported and if the
    version meets the minimum required version for the application. If the OS or
    version is not supported, it raises an EnvironmentError with an appropriate
    message.

    Raises:
        EnvironmentError: If the OS is unsupported ot the version does not meet
        the minimum required version.
    """
    
    os_name = platform.system()
    if os_name == 'Linux':
        os_version = get_linux_version()
        if not os_version:
            raise EnvironmentError("Unable to retrieve Linux version")
    else:
        os_version = platform.version()
    os_release = platform.release()
    
    # Checking supported operating systems
    supported_os = {
        'Windows': {'min_version': '10.0', 'patterns': [r'^[0-9]+\.[0-9]+$']},
        'Linux': {'min_version': '4.0', 'patterns': [r'^[0-9]+\.[0-9]+$', r'^[0-9]+\.[0-9]+\.[0-9]+$']}
    }
    
    if os_name not in supported_os:
        raise EnvironmentError(f"Unsupported operating system: {os_name}")
    
    os_info = supported_os[os_name]
    min_version = os_info['min_version']
    
    # Checking the OS version
    if not any(re.match(pattern, os_version) for pattern in os_info['patterns']):
        raise EnvironmentError(f"Unrecognized OS version: {os_version}")
    
    if not is_version_compatible(os_version, min_version):
        raise EnvironmentError(f"Minimum required version for {os_name} is {min_version}, but you have {os_version}")


def is_version_compatible(current_version, min_version):
    """is_version_compatible - Compare two versions to check compatibility.

    Extended Summary:
    This function compares the current OS version with the minimum required version
    to determine if the current version is greater than or equal to the minimum.
    The versions are expected to be in the format X.Y or X.Y.Z. The comparison is
    done by converting the version strings to tuple of integers and using the
    greater than or equal to (>=) operator.

    Arguments:
        current_version {str} -- The current version string.
        min_version {str} -- The minimum required version string.
    """

    def version_tuple(version_str):
        return tuple(map(int, version_str.split('.')))

    current_version_tuple = version_tuple(current_version)
    min_version_tuple = version_tuple(min_version)
    
    return current_version_tuple >= min_version_tuple
    