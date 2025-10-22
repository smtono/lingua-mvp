"""
Simply command line interface to
interact with database,
test primitive functionality, etc
"""

from dataclasses import dataclass
from cli.modules.user import UserCommand


@dataclass
class Command:
    """Commands to feed into command line interface for Lingua development"""

    def user(self, *args):
        """Direct to appropriate User command"""
        command = UserCommand(*args)
        print("...Parsing args...")
        command.parse()
        print("...Executing...")
        command.execute()

    def user_help(self):
        """Prints help for user command"""
        print("user")
        print("help - Prints this command")
        print("create <args> - Creates a hew user")

    def db(self, *args):
        """Direct to appropriate database command"""

    def db_help(self):
        """Prints help for db command"""
        print("db")
        print("help - Prints this command")

    def help_verbose(self, *args):
        """Print help for specified command"""
        module = args[0]
        getattr(Command, f"{module}_help")()

    command_map = {
        "help": help_verbose,
        "db": db,
        "user": user
    }


def cli():
    """
    Driver of command line interface
    """
    user_input = input("lingua>> ").split()
    command = user_input[0]
    command_args = user_input[1:]

    getattr(Command, command(command_args))
