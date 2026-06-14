# Interactive Arithmetic Desktop Application (Abacus Trainer)

A local e-learning desktop application built to support abacus education through interactive computation practice, validation logic, and performance tracking.

## Features

- **Practice Modules** – Generates arithmetic problems (addition, subtraction, multiplication) suited for abacus-based mental math practice.
- **Answer Validation** – Real-time validation logic checks user input against the correct answer.
- **Scoring System** – Tracks correct/incorrect answers and calculates a score for each session.
- **Performance History** – Stores session results in SQLite so students can track progress over time.
- **Event-Driven UI** – Built with Tkinter for a responsive, simple desktop experience.

## Tech Stack

| Component   | Technology |
|-------------|------------|
| Language    | Python     |
| UI Framework| Tkinter    |
| Database    | SQLite (SQL) |

## Project Structure

```
abacus-trainer/
├── src/
│   ├── main.py
│   ├── question_generator.py
│   ├── validator.py
│   ├── score_tracker.py
│   ├── database.py
│   └── schema.sql
├── README.md
└── .gitignore
```

## Database Schema

Session results are stored in the `sessions` table. See [`src/schema.sql`](src/schema.sql):

```sql
CREATE TABLE IF NOT EXISTS sessions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    difficulty      TEXT    NOT NULL,
    total_questions INTEGER NOT NULL,
    correct_answers INTEGER NOT NULL,
    accuracy        REAL    NOT NULL,
    timestamp       TEXT    NOT NULL
);
```

## How It Works

1. **Question Generation** – `question_generator.py` creates randomized arithmetic problems based on selected difficulty level.
2. **User Input** – The Tkinter UI (`main.py`) presents the question and accepts the user's answer.
3. **Validation** – `validator.py` checks the submitted answer against the correct result.
4. **Scoring** – `score_tracker.py` updates the running score and accuracy percentage.
5. **Persistence** – `database.py` saves each session's results (score, accuracy, timestamp) to SQLite for later review.

## Setup & Installation

### Prerequisites
- Python 3.8+
- Tkinter (usually included with Python)

### Steps

```bash
# Clone the repository
git clone https://github.com/dharshdiva/abacus-trainer.git
cd abacus-trainer

# Run the application
python src/main.py
```

No external dependencies are required — the app uses Python's built-in `tkinter` and `sqlite3` modules.

## Usage

1. Launch the app with `python src/main.py`.
2. Select a difficulty level (Easy / Medium / Hard).
3. Solve the displayed arithmetic problem and submit your answer.
4. View instant feedback (Correct / Incorrect) and your running score.
5. At the end of the session, view your accuracy summary, which is saved to the local database.

## Future Improvements

- Add timed practice mode with countdown
- Add difficulty-based leveling system that adapts to user performance
- Export performance reports as PDF/CSV
- Add multiplayer/competitive practice mode

## Author

**Divakar V**
[LinkedIn](#) | dharshrocky2004@gmail.com

## License

This project is licensed under the MIT License.
