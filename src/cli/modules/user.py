"""
User commands for CLI
"""

from command import Command


class UserCommand(Command):
    """
    User preferences command, edits user data

    Attributes:
    # TODO: update with attributes once decided upon
    """

    def parse(self):
        # test
        item = self.args
        print(item)
