"""
score_tracker.py

Tracks scoring and accuracy statistics during an abacus practice session.
"""


class ScoreTracker:
    """Tracks correct/incorrect answers and computes accuracy for a session."""

    def __init__(self):
        self.total_questions = 0
        self.correct_answers = 0

    def record_answer(self, is_correct):
        """
        Records the result of a single question.

        Args:
            is_correct (bool): Whether the user's answer was correct.
        """
        self.total_questions += 1
        if is_correct:
            self.correct_answers += 1

    def get_score(self):
        """Returns the number of correct answers."""
        return self.correct_answers

    def get_total(self):
        """Returns the total number of questions attempted."""
        return self.total_questions

    def get_accuracy(self):
        """
        Returns accuracy as a percentage (0-100).
        Returns 0 if no questions have been attempted.
        """
        if self.total_questions == 0:
            return 0.0
        return round((self.correct_answers / self.total_questions) * 100, 2)

    def reset(self):
        """Resets the tracker for a new session."""
        self.total_questions = 0
        self.correct_answers = 0
