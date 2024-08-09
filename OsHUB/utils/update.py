import requests


def get_latest_version(repository, current_version):
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
    
    url = f"https://api.github.com/repos/kduser12/{repository}/releases/latest"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        latest_version = data.get("tag_name", "undefined")
        
    except requests.exceptions.RequestException as error:
        print(f"HTTP request error: {error}")
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
    
    if current_version == latest_version:
        return False
    else:
        return latest_version


def check_versions(repository, current_version):
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
    
    result = get_latest_version(repository, current_version)
    return result