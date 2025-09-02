"""
Module for managing user profiles and tracking performance for a
language learning or quiz-based application

Classes:
    User:
        Represents an individual engaging with the program,
            including their Discord context,
        language preferences, proficiency level, and topics of interest
        This information is used to fine-tune quiz content
            and learning recommendations

    PerformanceTracker:
        Handles tracking user performance on quizzes and activities
        Updates user profiles, manages level progression,
            and stores relevant metrics
        to personalize future quizzes and monitor learning outcomes
"""


from dataclasses import dataclass


@dataclass
class User:
    """
    Represents a user interacting through Discord, including their
    language preference, proficiency level, and preferred topics

    Attributes:
        user_ctx: User context to provide when
            generating quizzes, updating preferences, and so on
        languages: Primary languages user is learning
        level: Current level of user
        topics: User input topics to use when generating quizzes
    """

    user_ctx: dict
    languages: list[str]
    level: int
    topics: list[str]

    def update_languages(self, new_language):
        """Check for valid language"""
        # TODO: finish proper docstrings

    def update_topics(self):
        """Updates topics user"""

    def update_languages(self):
        """Updates language preferences"""
