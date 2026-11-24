# Score Tracker Changes

## Summary

Updated `quiz.py` to save completed quiz results in a CSV file named
`score_history.csv` beside the program.

## Changes Made

- Added the standard-library `csv` and `datetime.date` imports.
- Added `SCORE_FILE = BASE_DIR / "score_history.csv"` for a working-directory-
  independent output location.
- Added `save_score()` to append one result row using these fields:
  `player_name`, `score`, `quiz_name`, `accuracy_percentage`, and `date`.
- Added a player-name prompt after a valid quiz has been loaded.
- Empty player names use `Unknown` as the stored fallback.
- Added accuracy calculation as a percentage after the quiz loop.
- Accuracy is formatted to two decimal places in the CSV and final output.
- Results are saved only after all selected questions have been answered.
- Added clear handling for CSV file-writing errors.
- Added a `Score saved.` confirmation after a successful write.
- The CSV header is written only when the file does not already exist.
