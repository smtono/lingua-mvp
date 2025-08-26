"""
Test user preferences changing through CLI execution
"""

from unittest import TestCase


class TestUserPreferences(TestCase):
    """
    Test User preferences
    """

    ##############################
    #   BASE CASE
    ##############################
    def test_update_context(self):
        """Updates user_ctx"""

    def test_update_languages(self):
        """Updates user languages"""

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
