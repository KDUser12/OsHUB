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

        :return Value:
        Nothing.
        """

        self.command    = command
        self.option     = option

        self.__str__()

        return

    def __str__(self):
        """Convert Object To String.

        :keyword Arguments:
        self                    -- This object.

        :return Value:
        Nicely formatted string to get information about this object.
        """

        print(f"\n\033[34m[\033[0m*\033[34m]\033[0m {self.option} - Tools :")

        for i in tools[self.command]:
            print(i)

        print(f"\n\033[34m[\033[0m*\033[34m]\033[0m {self.option} - Sites :")

        for i in sites[self.command]:
            print(i)

        return

