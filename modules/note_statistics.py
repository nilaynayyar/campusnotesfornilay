"""Utilities for calculating statistics about CampusNotes files."""

import os


def get_note_statistics(notes_dir="notes"):
    """Return the number of notes and total words across .txt and .md files."""
    if not os.path.isdir(notes_dir):
        return {"note_count": 0, "total_words": 0}

    note_count = 0
    total_words = 0

    for filename in sorted(os.listdir(notes_dir)):
        if filename.endswith((".txt", ".md")):
            filepath = os.path.join(notes_dir, filename)

            if os.path.isfile(filepath):
                try:
                    with open(filepath, "r", encoding="utf-8") as file:
                        total_words += len(file.read().split())
                    note_count += 1
                except (OSError, UnicodeDecodeError):
                    continue

    return {
        "note_count": note_count,
        "total_words": total_words
    }
