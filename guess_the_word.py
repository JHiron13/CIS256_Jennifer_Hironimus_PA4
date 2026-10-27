# Jennifer Hironimus
# CIS256 Fall 2026
# Programming Assignment 4

import random


# Words that the computer may choose from.
WORDS = [
    "python",
    "variable",
    "function",
    "testing",
    "github",
    "loop",
    "program"
]

MAX_WRONG_GUESSES = 6


def choose_word():
    """Choose and return a random word from the word list."""
    return random.choice(WORDS)


def create_display(word, guessed_letters):
    """Show guessed letters and hide letters not yet guessed."""
    display = []

    for letter in word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")

    return " ".join(display)
