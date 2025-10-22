"""
Test database interactions
"""

from unittest import TestCase
from app.sql.database import Database


class TestDatabase(TestCase):
    """
    Test Database functionality
    """

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.test_database = Database("test", "dummy.db")

    def test_database_exists(self):
        """
        Test opens database correctly
        """

    def test_database_nonexistent(self):
        """
        Test exception thrown for non existent database
        """
