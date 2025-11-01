"""
User commands for CLI
"""

from cli.modules.command import Command


class UserCommand(Command):
    """
    User preferences command, edits user data

    Attributes:
    """

    def parse(self):
        # Parse user args further for correct execution
        command = self.args[0]

        match command:
            case "create":  # Create new user
                # create <user> <{ctx}> <[languages]> <level> <[topics]>
                pass
            case "delete":  # Deletes existing user
                # delete <userId>
                pass
            case "update":  # Updates user
                # update <userId> <attribute> <change>
                pass
            case _:  # Either error or unsupported
                print("todo")

    def execute(self):
        pass
