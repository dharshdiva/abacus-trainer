"""
main.py

Entry point for the Interactive Arithmetic Desktop Application.
Provides a Tkinter-based UI for abacus practice sessions, including
question display, answer validation, scoring, and history tracking.
"""

import tkinter as tk
from tkinter import messagebox, ttk

from question_generator import QuestionGenerator
from validator import Validator
from score_tracker import ScoreTracker
from database import Database


class AbacusTrainerApp:
    """Main application window for the abacus practice tool."""

    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Arithmetic Trainer - Abacus Practice")
        self.root.geometry("420x320")
        self.root.resizable(False, False)

        self.db = Database()
        self.score_tracker = ScoreTracker()
        self.generator = None
        self.current_answer = None

        self._build_ui()

    def _build_ui(self):
        # Difficulty selection
        tk.Label(self.root, text="Select Difficulty:", font=("Arial", 12)).pack(pady=10)

        self.difficulty_var = tk.StringVar(value="easy")
        difficulty_combo = ttk.Combobox(
            self.root, textvariable=self.difficulty_var,
            values=["easy", "medium", "hard"], state="readonly"
        )
        difficulty_combo.pack(pady=5)

        start_btn = tk.Button(self.root, text="Start Session", command=self.start_session)
        start_btn.pack(pady=10)

        # Question display
        self.question_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        # Answer entry
        self.answer_entry = tk.Entry(self.root, font=("Arial", 14), justify="center")
        self.answer_entry.pack(pady=5)

        submit_btn = tk.Button(self.root, text="Submit Answer", command=self.submit_answer)
        submit_btn.pack(pady=10)

        # Score display
        self.score_label = tk.Label(self.root, text="Score: 0 / 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

    def start_session(self):
        difficulty = self.difficulty_var.get()
        self.generator = QuestionGenerator(difficulty)
        self.score_tracker.reset()
        self._next_question()

    def _next_question(self):
        if self.generator is None:
            messagebox.showwarning("No session", "Please start a session first.")
            return

        question_text, answer = self.generator.generate_question()
        self.current_answer = answer
        self.question_label.config(text=question_text)
        self.answer_entry.delete(0, tk.END)

    def submit_answer(self):
        if self.generator is None:
            messagebox.showwarning("No session", "Please start a session first.")
            return

        user_input = self.answer_entry.get()

        if not Validator.is_valid_number(user_input):
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        is_correct = Validator.is_correct(user_input, self.current_answer)
        self.score_tracker.record_answer(is_correct)

        if is_correct:
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer was {self.current_answer}.")

        self._update_score_display()

        # Save progress and load next question
        self.db.save_session(
            self.difficulty_var.get(),
            self.score_tracker.get_total(),
            self.score_tracker.get_score(),
            self.score_tracker.get_accuracy()
        )
        self._next_question()

    def _update_score_display(self):
        score = self.score_tracker.get_score()
        total = self.score_tracker.get_total()
        accuracy = self.score_tracker.get_accuracy()
        self.score_label.config(text=f"Score: {score} / {total}  (Accuracy: {accuracy}%)")


def main():
    root = tk.Tk()
    app = AbacusTrainerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
