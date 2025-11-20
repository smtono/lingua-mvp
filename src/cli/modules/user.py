"""
User commands for CLI
"""

import os

from pathlib import Path

from cli.modules.command import Command
from app.sql.database import Database


class UserCommand(Command):
    """
    User preferences command, edits user data

    Attributes:
        db: User table in database
    """

    def __init__(self, user_input):
        super().__init__(user_input)
        self.db = Database("", Path(os.getcwd(), "app", "db", "users"))

    def parse(self):
        # Parse user args further for correct execution
        command = self.args[0]
        cmd_args = self.args[1:]

        # Validate cmd args

        match command:
            case "create":  # Create new user
                # create <user> <{ctx}> <[languages]> <level> <[topics]>
                flags = ""
                self.execute_create()
            case "delete":  # Deletes existing user
                # delete <userId>
                self.execute_delete()
            case "update":  # Updates user
                # update <userId> <attribute> <change>
                self.execute_update()
            case _:  # Either error or unsupported
                print("todo")

    def parse_create(self):
        pass
    
    def parse_delete(self):
        pass
    
    def parse_update(self):
        pass

    def execute_create(self):
        self.db.insert_data("", "", "")

    def execute_delete(self):
        self.db.update_table("", "")

    def execute_update(self):
        self.db.update_table("", "")
