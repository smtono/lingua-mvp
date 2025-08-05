"""
Module for managing user profiles and tracking performance for a
language learning or quiz-based application.

Classes:
    User:
        Represents an individual engaging with the program,
            including their Discord context,
        language preferences, proficiency level, and topics of interest.
        This information is used to fine-tune quiz content
            and learning recommendations.

    PerformanceTracker:
        Handles tracking user performance on quizzes and activities.
        Updates user profiles, manages level progression,
            and stores relevant metrics
        to personalize future quizzes and monitor learning outcomes.
"""


class User:
    """
    Represents a user interacting through Discord, including their
    language preference, proficiency level, and preferred topics.
    """

    def __init__(self,
                 user_ctx: dict,
                 language: str,
                 level: int,
                 topics: list[str]):
        """
        Initializes a User instance.

        Args:
            user_ctx (dict): Metadata for the user.
            language (str): The language the user is interested in or uses.
            level (int): The user's language proficiency level.
            topics (list[str]): List of topics the user prefers.
        """
        self.user_ctx = user_ctx
        self.language = language
        self.level = level
        self.topics = topics
