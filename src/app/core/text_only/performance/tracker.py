"""
Tracks performance of user quiz results
"""


class PerformanceTracker:
    """
    Tracks user performance and manages profile updates
        based on quiz results and activity.
    Responsible for leveling up users, updating their profile,
        and maintaining performance metrics.

    Attributes:
        user: User object to validate results on
        cursor: Database object to fetch user data and ranking from
        quiz: Current quiz the user is taking with results
    """

    def __init__(self, user, cursor, quiz):
        self.user = user
        self.cursor = cursor
        self.quiz = quiz

    def assess_results(self):
        """
        Grade user's quiz and gives appropriate rankings back
        """

    def markup(self):
        """
        Marks up quiz to create a harder ranking one
        Returns results/assessment of quiz results
        """

    def update_user(self):
        """Levels up user after test"""
