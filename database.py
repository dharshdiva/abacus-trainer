"""
database.py

Handles SQLite persistence for storing abacus practice session results,
allowing students to track their performance history over time.
"""

import sqlite3
from datetime import datetime


class Database:
    """Manages SQLite storage for practice session results."""

    def __init__(self, db_path="abacus_sessions.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                difficulty TEXT NOT NULL,
                total_questions INTEGER NOT NULL,
                correct_answers INTEGER NOT NULL,
                accuracy REAL NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def save_session(self, difficulty, total_questions, correct_answers, accuracy):
        """
        Saves a completed practice session to the database.

        Args:
            difficulty (str): The difficulty level of the session.
            total_questions (int): Total number of questions attempted.
            correct_answers (int): Number of correctly answered questions.
            accuracy (float): Accuracy percentage for the session.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO sessions (difficulty, total_questions, correct_answers, accuracy, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (difficulty, total_questions, correct_answers, accuracy, datetime.now().isoformat()))
        conn.commit()
        conn.close()

    def get_history(self, limit=10):
        """
        Retrieves the most recent practice sessions.

        Args:
            limit (int): Maximum number of records to return.

        Returns:
            list[tuple]: List of session records.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT difficulty, total_questions, correct_answers, accuracy, timestamp
            FROM sessions
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))
        rows = cursor.fetchall()
        conn.close()
        return rows
