"""
Abstract command class for CLI
"""

from abc import ABC


class Command(ABC):
    """
    Base command with simple execute and parse functionality

    Attributes:
        command: Command module to execute
        args: Arguments to pass to command module
    """

    def __init__(self, user_input: str):
        super().__init__()
        parsed_args = user_input.split()
        self.command = parsed_args[0]
        self.args = parsed_args[1:]

    def parse(self):
        """
        Further parse passed in arguments
        """

    def execute(self):
        """
        Executes given command
        """
