#!/usr/bin/env python3

import platform
import subprocess
import logging
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
        return version
    except subprocess.CalledProcessError as error:
        logging.error(f"Failed to get Linux version: {error}")
    return None


def check_os_compatibility():
    """check_os_compatibility - Check the compatibility of the current operating system.

    Extended Summary:
    This function determines the current operating system and version, logging the
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
            logging.error("Unable to retrieve Linux version")
            raise EnvironmentError("Unable to retrieve Linux version")
    else:
        os_version = platform.version()
    os_release = platform.release()

    logging.debug(f"Detected operating system: {os_name}")
    logging.debug(f"Detected version: {os_version}")
    logging.debug(f"Detected release: {os_release}")

    # Checking supported operating systems
    supported_os = {
        'Windows': {'min_version': '10.0', 'patterns': [r'^[0-9]+\.[0-9]+$']},
        'Linux': {'min_version': '4.0', 'patterns': [r'^[0-9]+\.[0-9]+$', r'^[0-9]+\.[0-9]+\.[0-9]+$']},
        'Darwin': {"min_version": '19.0', 'patterns': [r'^[0-9]+\.[0-9]+$']}
    }

    if os_name not in supported_os:
        logging.error(f"Unsupported operating system: {os_name}")
        raise EnvironmentError(f"Unsupported operating system: {os_name}")

    os_info = supported_os[os_name]
    min_version = os_info['min_version']

    logging.debug(f"Minimum required version for {os_name}: {min_version}")

    # Checking the OS version
    if not any(re.match(pattern, os_version) for pattern in os_info['patterns']):
        logging.error(f"Unrecognized OS version: {os_version}")
        raise EnvironmentError(f"Unrecognized OS version: {os_version}")

    if not is_version_compatible(os_version, min_version):
        logging.error(f"Minimum required version for {os_name} is {min_version}, but you have {os_version}")
        raise EnvironmentError(f"Minimum required version for {os_name} is {min_version}, but you have {os_version}")

    logging.info(f"Operating system: {os_name} {os_version} ({os_release})")


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

    logging.debug(f"Comparing versions: current ({current_version_tuple}) >= minimum ({min_version_tuple})")

    return current_version_tuple >= min_version_tuple
