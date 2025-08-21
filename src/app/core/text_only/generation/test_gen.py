"""
Test Generation

A test will showcase the user's skill and
update accordingly after the conclusion of it
Test will take in user's "stats" and grab/generate data pertaining to it
Test results will be stored and used to calculate what user needs to review
"""


class TestGenerator:
    """
    Generates tests for a given User

    Attributes:
        user: User to create the test for
        cursor: The database object to fetch user preferences and level
    """

    def __init__(self, user, cursor):
        self.user = user
        self.cursor = cursor

    def generate(self):
        """Generates a test"""

    def followup(self):
        """Follows up after test to give increased difficulty test"""
