"""
Simply command line interface to
interact with database,
test primitive functionality, etc
"""

from dataclasses import dataclass


@dataclass
class Command:
    """Commands to feed into command line interface for Lingua development"""

    def user(self, *args):
        """Direct to appropriate User command"""
        # if "update" in args, call user_update

    def user_create(self):
        """TODO: add appropriate args
        Creates user with given args"""

    def db(self, *args):
        """Direct to appropriate database command"""

    def db_user_update(self):
        """TODO: add appropriate args
        Updates user with given args"""

    def db_user_get(self):
        """TODO: add appropriate args
        Fetches user with given args"""

    def help_verbose(self, *args):
        """Print help for specified command"""

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
