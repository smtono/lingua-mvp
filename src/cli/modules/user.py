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
        cmd_args = self.args[1:]

        # Validate cmd args

        match command:
            case "create":  # Create new user
                # create <user> <{ctx}> <[languages]> <level> <[topics]>
                ctx = ""
                languages = ""
                level = 0
                topics = ""
                self.execute_create()
            case "delete":  # Deletes existing user
                # delete <userId>
                userId = cmd_args[0]
                self.execute_delete()
            case "update":  # Updates user
                # update <userId> <attribute> <change>
                userId = cmd_args[0]
                attribute = cmd_args[1]
                change = cmd_args[2:]
                self.execute_update()
            case _:  # Either error or unsupported
                print("todo")

    def execute_create(self):
        pass

    def execute_delete(self):
        pass
    
    def execute_update(self):
        pass
