import logging
import requests

from __init__ import forge_api_latest_release


def get_latest_version(current_version):
    """get_latest_version - Retrieve the latest release version from a GitHub repository.

    Extended Summary:
    This function sends a GET request to the GitHub API to fetch the latest release version
    of a specified repository. It checks if the retrieved version follows the expected format.
    If the format is invalid or if there is an error in the HTTP request, the function logs
    the issue and returns None. Otherwise, it returns the result of comparing the current
    version with the latest version.

    Arguments:
        repository {str} -- The GitHub repository in the format 'owner/repo'.
        current_version {str} -- The current version of the software.

    Returns:
        str or None -- The latest version if a new version is available, False if up-to-date, or None if there is an error.
    """

    url = forge_api_latest_release

    try:
        logging.debug(f"GET request sent to URL: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        latest_version = data.get("tag_name", "undefined")

        logging.debug(f"Latest version retrieved: {latest_version}")

    except requests.exceptions.RequestException as error:
        logging.error(f"HTTP request error: {error}")
        return None

    return get_result_version(current_version, latest_version)


def get_result_version(current_version, latest_version):
    """get_result_version - Compare current version with the latest version to determine update status.

    Extended Summary:
    This function compares the current version of the software with the latest version available.
    It logs whether the current version is up-to-date or if a new version is available. If the
    current version does not conform to the expected format, it logs an error and returns None.

    Arguments:
        current_version {str} -- The current version of the software.
        latest_version {str} -- The latest available version of the software.

    Returns:
        str, bool or None -- The latest version if a new version is available, False if up-to-date, or None if there is an error.
    """

    logging.debug(f"Comparing current version ({current_version}) with the latest version ({latest_version})")

    if current_version == latest_version:
        logging.info(f"Current version ({current_version}) is up to date.")
        return False
    else:
        return latest_version


def check_versions(current_version):
    """check_versions - Check the version for a single repository.

    Extended Summary:
    This function checks the latest release version for a single GitHub repository and
    compares it with the current version. It logs the result and returns whether the current
    version is up-to-date or if a new version is available.

    Arguments:
        repository {str} -- The GitHub repository in the format 'owner/repo'.
        current_version {str} -- The current version of the software.

    Returns:
        str or None -- The latest version if a new version is available and valid, otherwise None.
    """

    logging.debug(f"Checking version for repository {forge_api_latest_release}")
    result = get_latest_version(current_version)
    return result