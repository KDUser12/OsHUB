#!/usr/bin/env python3

import logging
import pkg_resources  # type: ignore
import subprocess
import sys


def parse_requirements(file):
    """parse_requirements - Parse the requirements file to extract packages and versions.

    Extended Summary:
    This function reads a requirements file, ignoring comments and empty lines,
    and extracts the package names and version specifications. Each line is stripped
    of leading and trailing whitespace before being added to the list of requirements.

    Arguments:
        file {str} -- The path to the requirements file.

    Returns:
        list of str -- A list of package names and versions extracted from the file.
    """

    logging.debug(f"Reading requirements file: {file}")
    with open(file, 'r') as f:
        lines = f.readlines()

    requirements = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            logging.debug(f"Found package: {line}")
            requirements.append(line)
    return requirements


def check_and_install_dependencies(requirements_files):
    """check_and_install_dependencies - Check dependencies and install them if necessary.

    Extended Summary:
    This function processes a list of requirements files to determine which packages
    and versions are required. It compares the required packages against the installed
    packages and versions. Missing or incorrect packages are identified and installed
    using pip. the function logs the details of the packages checked and any actions
    taken during the process.

    Arguments:
        requirements_files {list of str} -- A list of paths to requirements files.
    """

    required_packages = []
    for file in requirements_files:
        required_packages.extend(parse_requirements(file))

    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    logging.debug(f"Installed packages: {installed_packages}")

    missing_packages = []
    for req in required_packages:
        try:
            pkg_info = pkg_resources.Requirement.parse(req)
            pkg_name = pkg_info.project_name.lower()
            pkg_version = pkg_info.specifier
            installed_version = installed_packages.get(pkg_name)

            logging.debug(f"Checking package: {pkg_name} with installed version: {installed_version}")

            if installed_version:
                if not pkg_version.contains(installed_version):
                    logging.info(
                        f"Package {pkg_name} version {installed_version} does not meet the required version {pkg_version}.")
                    missing_packages.append(req)
            else:
                logging.info(f"Package {pkg_name} is not installed.")
                missing_packages.append(req)
        except Exception as error:
            logging.error(f"Error parsing {req}: {error}")

    if missing_packages:
        logging.info(f"Missing or incorrect packages: {', '.join(missing_packages)}")

        try:
            logging.info("Installing missing packages...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing_packages])
            logging.info("Installation complete.")
        except subprocess.CalledProcessError as error:
            logging.error(f"Error during installation: {error}")
    else:
        logging.info("All dependencies are installed.")
