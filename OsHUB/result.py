from colorama import Fore

from resources.tools import tools
from resources.sites import sites


def check_value(dictionary: dict) -> bool:
    """Checking dictionary values.

    Args:
        dictionary (dict): Dictionary to process

    Returns:
        bool: result of dictionary check
    """

    if isinstance(dictionary, dict):
        return any(bool(inner) for inner in dictionary.values())
    elif isinstance(dictionary, set):
        return bool(dictionary)
    else:
        return False


class QueryResult:
    """Query Result Object.
    Describes result of query about a given value.
    """

    def __init__(self, command: int, option: str) -> None:
        """Create a query result object.
        Contains information about a specific display method on a given type of website and tool.

        Args:
            command (int): Int value containing the command entered by the user
            option (str): Str value containing the option
        """

        self.command = command
        self.option = option

        print(self.format_output())

    def format_output(self) -> str:
        """Format the output string.

        Returns:
            str: formatted string with information about this object.
        """

        formatted_output = ""
        if check_value(tools[self.command]):
            formatted_output = formatted_output + f"\n{Fore.BLUE}[{Fore.RESET}*{Fore.BLUE}]{Fore.RESET} {self.option} - Tools :"
            for tool in tools[self.command]:
                formatted_output = formatted_output + f"\n- {tool}"

        if check_value(sites[self.command]):
            if check_value(tools[self.command]):
                formatted_output = formatted_output + "\n"

            formatted_output = formatted_output + f"\n{Fore.BLUE}[{Fore.RESET}*{Fore.BLUE}]{Fore.RESET} {self.option} - Sites :"
            for site in sites[self.command]:
                formatted_output = formatted_output + f"\n- {site}"
        
        return formatted_output
        
    def __str__(self) -> str:
        """Convert Object to string.

        Returns:
            str: formatted string with information about this object.
        """

        return f"QueryResult(command={self.command}, option={self.option})"
