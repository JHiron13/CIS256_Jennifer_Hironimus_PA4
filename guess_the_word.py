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

def process_guess(word, guess, guessed_letters):
    """Store a guess and return True if it appears in the word."""
    guessed_letters.add(guess)

    if guess in word:
        return True

    return False


def word_is_complete(word, guessed_letters):
    """Return True when every letter in the word has been guessed."""
    for letter in word:
        if letter not in guessed_letters:
            return False

    return True
