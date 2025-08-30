"""
Test user preferences changing through CLI execution
"""

from unittest import TestCase
from app.user.user_preferences import UserPreferences
from app.user.user import User
from app.user.sql.database import Database


class TestUserPreferences(TestCase):
    """
    Test User preferences
    """

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.test_database = Database("test.db")
        self.dummy_user = User(
            {"static_key": "variable_value"}, ["en", "jp"], 2, ["food"]
        )

    ##############################
    #   BASE CASE
    ##############################
    def test_update_context(self):
        """Updates user_ctx"""
        preferences = UserPreferences(self.dummy_user, self.test_database)
        preferences.update_preferences()

        # Assert context changed
        # TODO

    def test_update_languages(self):
        """Updates user languages"""
        new_language = "korean"
        self.dummy_user.update_languages(new_language)

        # Assert context changed
        # TODO

    def test_update_level(self):
        """Updates user level"""

    ##############################
    #   SPECIAL CASE
    ##############################
    def test_update_context_topic(self):
        """Tests for topic update"""

    ##############################
    #   THROWS EXCEPTION
    ##############################
    def test_update_context_invalid(self):
        """Test invalid case of context update"""

    def test_update_context_topic_invalid(self):
        """Test invalid case of context for topic update"""

    def test_update_languages_invalid(self):
        """Tests for nonexistent/unsupported language"""
