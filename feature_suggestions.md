# Suggested Trivia Program Features

These suggestions build on the current quiz selection, Markdown question files,
random question selection, and answer checking. They are separate from the
ideas already listed in `improvements.md`.

## 1. Shuffle Answer Choices

Randomize the order of the choices for each question each time a quiz runs.
Keep the correct answer tied to its choice text so scoring remains accurate
even when the displayed A-D labels change.

## 2. Show Answer Explanations

Allow question files to include a short explanation, optionally with a source
link, for each correct answer. After each response, display the explanation
alongside the correct answer to make the quiz more useful for learning.

## 3. Validate Quiz Files Before Starting

Check each selected Markdown file for common formatting problems, such as
missing choices, duplicate choice labels, invalid answer-key letters, or
questions without an answer. Report the affected question numbers and explain
what needs correction instead of silently leaving unusable questions out.
