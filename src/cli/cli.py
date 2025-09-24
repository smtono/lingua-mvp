"""
Simply command line interface to
interact with database,
test primitive functionality, etc
"""

class Command:
    def user():
        pass

    def db():
        pass

    def help_verbose():
        pass

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
