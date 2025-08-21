"""
Recommendation Engine

Validate user input and provide feedback
Has a fact checking component to it
"""


class RecommendationEngine:
    """
    Updates user's data based on passed arguments on recommendations

    Attributes:
        user: User object to update in database
        cursor: Database object to update with
    """

    def __init__(self, user, cursor):
        self.user = user
        self.cursor = cursor

    def update_on(self, args):
        """
        Update on args of args
        """

    def give(self):
        """Placeholder for giving output of engine"""
