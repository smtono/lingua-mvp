"""
User represents someone engaging with the program and information about them
This information is used to fine tune what the quizzes will look like based on:
    - Language
    - Skill
    - Desired topics
    - Etc
"""

class User:
    """
    e
    """
    def __init__(self):
        self.username = ""
        self.language = ""
        self.level = 0
        self.topics = []
