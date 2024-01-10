import requests


def get_latest_version(repository, current_version):
    """
    Get the latest version of the repository from GitHub.

    :param repository:      Name of the GitHub repository
    :param current_version: Current version of the application

    :return:                A message indicating whether an update is available or an error occurred.
    """

    url = f'https://api.github.com/repos/KDUser12/{repository}/releases/latest'

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        latest_version = data['tag_name']

        return check_version(current_version, latest_version)
    except requests.exceptions.RequestException as error:
        return f"Error retrieving KDUser12/{repository} information: {error}"


def check_version(current_version, latest_version):
    """
    Check if a new version is available.

    :param current_version: Current version of the application.
    :param latest_version:  Latest version fetched from GitHub.

    :return: A message indicating whether an update is available.
    """

    if current_version == latest_version:
        return False
    else:
        return f"A new version ({latest_version}) is available. Please update your project."

# Example usage:
# latest_version_message = get_latest_version("AvCalculator", "2.0.0")
# print(latest_version_message)
