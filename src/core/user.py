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
                 discord_ctx: dict,
                 language: str,
                 level: int,
                 topics: list[str]):
        """
        Initializes a User instance.

        Args:
            discord_ctx (dict): Discord context or metadata for the user.
            language (str): The language the user is interested in or uses.
            level (int): The user's language proficiency level.
            topics (list[str]): List of topics the user prefers.
        """
        self.discord_ctx = discord_ctx
        self.language = language
        self.level = level
        self.topics = topics


class PerformanceTracker:
    """
    Tracks user performance and manages profile updates
        based on quiz results and activity.
    Responsible for leveling up users, updating their profile,
        and maintaining performance metrics.
    """

    def __init__(self):
        pass
