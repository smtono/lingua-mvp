"""
User commands for CLI
"""

from command import Command


class UserCommand(Command):
    """
    User preferences command, edits user data

    Attributes:
    """

    def parse(self):
        # test
        item = self.args
        print(item)

    def execute(self):
        pass
