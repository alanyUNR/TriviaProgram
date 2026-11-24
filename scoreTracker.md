# Score Tracker CSV Updates

Add score history to `quiz.py` so each completed quiz attempt saves the player's
name, score, quiz name, accuracy percentage, and completion date.

## 1. Add the Required Imports

Add the Python standard-library modules for CSV output and dates near the top
of `quiz.py`:

```python
import csv
from datetime import date
```

`csv` safely handles commas and quotation marks in values, while `date` creates
an ISO-formatted date such as `2026-11-23`.

## 2. Get the Player's Name

Add a prompt in `main()` after a valid quiz file has been selected and loaded:

```python
player_name = input("Player name: ").strip()
```

If an empty name is entered, keep prompting or use a clearly marked fallback
such as `"Unknown"`. The name should be stored exactly as entered rather than
being combined with the score or quiz name.

## 3. Calculate and Store the Result

After the quiz loop has ended, calculate:

- **Score:** `correct`
- **Quiz name:** `question_file.stem`
- **Accuracy:** `(correct / len(quiz_questions)) * 100`
- **Date:** `date.today().isoformat()`

Use the quiz name without the `.md` extension, for example `renoQuestions`,
and format the accuracy with one or two decimal places. Do not calculate
accuracy when `len(quiz_questions)` is zero.

Then call a CSV-writing function:

```python
save_score(player_name, correct, question_file.stem,
           accuracy, date.today().isoformat())
```

The existing result print statement can remain and may include the accuracy:

```python
print(f"Results: {correct} correct, "
      f"{len(quiz_questions) - correct} incorrect.")
print(f"Accuracy: {accuracy:.2f}%")
```

## 4. Create a CSV-Writer Function

Define `save_score()` in `quiz.py`, preferably near `is_correct()`:

```python
SCORE_FILE = BASE_DIR / "score_history.csv"


def save_score(player_name, score, quiz_name, accuracy, completed_date):
    fieldnames = ["player_name", "score", "quiz_name",
                  "accuracy_percentage", "date"]

    file_exists = SCORE_FILE.exists()
    with SCORE_FILE.open("a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "player_name": player_name,
            "score": score,
            "quiz_name": quiz_name,
            "accuracy_percentage": f"{accuracy:.2f}",
            "date": completed_date,
        })
```

Use `BASE_DIR`, already defined in `quiz.py`, so the CSV is saved beside the
program and Markdown files regardless of which working directory starts the
program. The CSV file should be named `score_history.csv` and opened in append
mode so completed quizzes are added rather than replacing previous results.

## 5. CSV Format

The resulting file should use these header fields and one row per completed
quiz:

```csv
player_name,score,quiz_name,accuracy_percentage,date
Alice,4,renoQuestions,80.00,2026-11-23
```

Score should be an integer, accuracy should be numeric, and date should use
`YYYY-MM-DD`. The CSV writer will automatically quote fields that contain a
comma or double quotation mark.

## 6. Error and Completion Handling

- Save the result only after all selected questions have been answered.
- Do not append a row if the quiz has no usable questions.
- Handle file-writing errors with a clear message instead of silently failing.
- Return a success or failure indicator from `save_score()` if the program will
  display a confirmation such as `"Score saved."`
- Confirm a successful save after the final result is printed.
