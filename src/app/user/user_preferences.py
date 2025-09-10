"""
Updates to user preferences interacting with the database
"""


from app.user.sql.database import Database
from app.user.user import User


class UserPreferences:
    """
    Changes attributes of User's preferences
    based on passed in User object and commands

    Attributes:
        user: User object to edit preferences of in the database
        cursor: Database object to execute queries with
    """

    def __init__(self, user: User, cursor: Database):
        self.user = user
        self.cursor = cursor

    def update_preferences(self, new_preferences):
        """Fetches User data from the DB and updates accordingly"""
        self.user.topics.append(new_preferences)

    def get_preferences(self, user):
        """Fetches user data to return back to user"""
