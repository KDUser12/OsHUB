from ressources.tools import tools
from ressources.sites import sites


class QueryResult:
    """Query Result Object.

    Describes result of query about a given value.
    """
    def __init__(self, command, option):
        """Create a query result object.

        Contains information about a specific display method on
        a given type of website and tool.

        :param command:     --  INT value containing the command entered
                                by the user.
        :param option:      --  STR value containing the option.

        :return:            --  None
        """

        self.command = command
        self.option = option
        self.format_output()

    def format_output(self):
        """Format the output string.

        :return:    Formatted string with information about this object.
        """

        if self.command == 11:
            print("\033[31mWarning - If you decide to access the tools/sites we offer you your image of the"
                  "reality may change forever (not recommended for sensitive people.)\033[0m")
            print(
                "\033[31mAvertissement - Si vous décidez d’accéder aux outils / sites que nous vous proposons votre image de"
                " la réalité peut changer pour toujours (non recommandé pour les personnes sensibles.)\033[0m")
            if not input("Please choose an option [y] / [n]") == "y":
                return

        formatted_output = f"\n\033[34m[\033[0m*\033[34m]\033[0m {self.option} - Tools :"

        for i in tools[self.command]:
            formatted_output += f"\n{i}"

        formatted_output += f"\n\n\033[34m[\033[0m*\033[34m]\033[0m {self.option} - Sites :"

        for i in sites[self.command]:
            formatted_output += f"\n{i}"

        print(formatted_output)

    def __str__(self):
        """Convert Object To String.

        :return: Formatted string with information about this object.
        """
        return f"QueryResult(command={self.command}, option={self.option})"

