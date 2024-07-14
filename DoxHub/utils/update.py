import requests
from colorama import Fore


def get_latest_version(current_version: str):
    """Get the latest version of the repository from GitHub.

    Args:
        current_version (str): Current version of the application.

    Returns:
        str: potential update or possible error
    """

    try:
        response = requests.get("https://api.github.com/repos/kduser12/doxhub/releases/latest")
        response.raise_for_status()

        data = response.json()
        latest_version = data['tag_name']
    
    except requests.exceptions.HTTPError as http_err:
        return f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} An error occurred: {req_err}"
    
    return check_for_update(current_version, latest_version)
    

def check_for_update(current_version: str, latest_version: str):
    """Check if a new version is available.

    Args:
        current_version (str): Current version of the application
        latest_version (str): Latest version fetched from GitHub

    Returns:
        str: potential update
    """

    if current_version != latest_version:
        return f"Install the latest DoxHub ({latest_version}) for new features and improvements! https://github.com/KDUser12/DoxHub/releases/latest"
    return False
