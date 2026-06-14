"""
question_generator.py

Generates randomized arithmetic questions for abacus practice sessions,
based on a selected difficulty level.
"""

import random


class QuestionGenerator:
    """Generates arithmetic problems suited for abacus mental-math practice."""

    DIFFICULTY_RANGES = {
        "easy": (1, 20),
        "medium": (10, 100),
        "hard": (50, 999),
    }

    OPERATORS = ["+", "-", "*"]

    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty.lower()
        if self.difficulty not in self.DIFFICULTY_RANGES:
            raise ValueError(f"Unknown difficulty: {difficulty}")

    def generate_question(self):
        """
        Returns a tuple: (question_text, correct_answer)
        """
        low, high = self.DIFFICULTY_RANGES[self.difficulty]
        a = random.randint(low, high)
        b = random.randint(low, high)
        operator = random.choice(self.OPERATORS)

        if operator == "+":
            answer = a + b
        elif operator == "-":
            # Ensure non-negative result for simplicity
            a, b = max(a, b), min(a, b)
            answer = a - b
        else:  # multiplication
            # Keep multiplication operands small for usability
            b = random.randint(1, 12)
            answer = a * b

        question_text = f"{a} {operator} {b} = ?"
        return question_text, answer
