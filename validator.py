"""
validator.py

Provides validation logic for checking user-submitted answers
against expected results during abacus practice sessions.
"""


class Validator:
    """Validates user answers against the correct result."""

    @staticmethod
    def is_correct(user_input, correct_answer):
        """
        Checks whether the user's input matches the correct answer.

        Args:
            user_input (str): Raw text entered by the user.
            correct_answer (int): The expected correct answer.

        Returns:
            bool: True if correct, False otherwise.
        """
        try:
            user_value = int(user_input.strip())
        except (ValueError, AttributeError):
            return False

        return user_value == correct_answer

    @staticmethod
    def is_valid_number(user_input):
        """
        Checks whether the given input string represents a valid integer.
        """
        try:
            int(user_input.strip())
            return True
        except (ValueError, AttributeError):
            return False
