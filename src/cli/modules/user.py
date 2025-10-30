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
                pass
            case "delete":  # Deletes existing user
                pass
            case "":
                pass
            case _:  # Either error or unsupported
                print("todo")

    def execute(self):
        pass
