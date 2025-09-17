"""
This module is used to define the database for the system
As well as functions used to interact with the database
This system uses a SQLite database

TODO: fix warnings/more descriptive error logging
TODO: Add validation checks for queries to avoid SQL injection
TODO: Fix raised exceptions to be more descriptive
"""

import logging
import sqlite3
import os
from sqlite3 import Error
from pathlib import Path
from typing import Optional


class Database:
    """
    This class is used to create a database and manipulate it.

    Attributes:
        connector: SQLite instance to connect to
        cursor: Cursor object to execute queries with
    """

    def __init__(self, db_name: str, path: Optional[str]) -> None:
        # Initialize working directory
        if not path:
            db_path = Path(os.getcwd(), "database")
        else:
            db_path = Path(path)

        self.db_path = db_path
        self.connector = sqlite3.connect(f"{db_path}/{db_name}.db")
        self.cursor = self.connector.cursor()

    def create_db(self, db_name: str):
        """
        Creates a database with the given name

        Args:
            db_name: str
                The name of the database to be created
        """
        with open(f"{self.db_path}/{db_name}.db", "w+", encoding="UTF-8"):
            self.connector = sqlite3.connect(f"{self.db_path}/{db_name}.db")
            self.cursor = self.connector.cursor()

    #######################
    # Query Manipulation
    ########################
    def select_data(self, query_for: str, query_table: str):
        """
        Selects data from a table

        Args:
            query_for: The data to be queried
            query_table: The table to be queried
        """
        try:
            self.cursor.execute(f"SELECT {query_for} FROM {query_table};")
            res = self.cursor.fetchall()
            print(res)
            return res
        except Error as err:
            if err != 0:
                logging.warning(
                    "Problem with table Select"
                    "(Is query asking for correct table?)"
                )
            else:
                logging.error("An unknown problem has occured.")

    def insert_data(self, table_name: str, columns: str, data: str):
        """
        Inserts data into a table

        Args:
            table_name: str
                The name of the table to be updated
            columns: str
                The columns to be updated
            data: str
                The data to be inserted
        """
        try:
            self.cursor.execute(
                f"INSERT INTO {table_name}" f"({columns}) VALUES ({data});"
            )
        except Error as err:
            if err != 0:
                logging.warning(
                    "Problem with Data Insertion"
                    "(Is table and columns correct?)"
                )
            else:
                logging.error("An unknown problem has occured.")

    def custom_query(self, sql_query: str):
        """
        Executes a custom query

        Args:
            sql_query: str
                The query to be executed
        """
        try:
            self.cursor.execute(sql_query)
        except Error as err:
            if err != 0:
                logging.warning(
                    "Problem with Custom Query"
                    "(Incorrect command?)"
                )
            else:
                logging.error("An unknown problem has occured.")

    #######################
    # Table Manipulation
    ########################
    def create_table(self, table_name: str, table_args: str):
        """
        Creates a table with the given name

        Args:
            table_name: str
                The name of the table to be created
            table_args: str
                The arguments for the table to be created
        """
        try:
            self.cursor.execute(f"CREATE TABLE {table_name} ({table_args});")
        except Error as err:
            if err != 0:
                logging.warning("Table already exists")
            else:
                logging.error("An unknown problem has occured.")

    def alter_table(self, table_name: str, table_args: str):
        """
        Alters a table with the given name

        Args:
            table_name: str
                The name of the table to be altered
            table_args: str
                The arguments for the table to be altered
        """
        try:
            self.cursor.execute(f"ALTER TABLE {table_name} {table_args}")
        except Error as err:
            if err != 0:
                logging.warning(
                    "Problem with table Alter"
                    "(Is table name correct?)"
                )
            else:
                logging.error("An unknown problem has occured.")

    def delete_table(self, table_name: str):
        """
        Deletes a table with the given name

        Args:
            table_name: str
                The name of the table to be deleted
        """
        try:
            self.cursor.execute(f"DROP TABLE {table_name}")
        except Error as err:
            if err != 0:
                logging.warning(
                    "Problem with table Delete (Is table name correct?)"
                )
            else:
                logging.error("An unknown problem has occured.")

    def update_table(self, table_name: str, data_args: str):
        """
        Updates a table with the given name

        Args:
            table_name: str
                The name of the table to be updated
            data_args: str
                The arguments for the table to be updated
        """
        try:
            self.cursor.execute(f"UPDATE {table_name} SET {data_args}")
        except Error as err:
            if err != 0:
                logging.warning(
                    "Problem with table Update"
                    "(Is table name correct?)"
                )
            else:
                logging.error("An unknown problem has occured.")
