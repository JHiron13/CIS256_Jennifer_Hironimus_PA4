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

def play_game():
    """Run the main word guessing game."""

    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to the Word Guessing Game!")
    print("Guess the hidden word one letter at a time.")

    while (
        wrong_guesses < MAX_WRONG_GUESSES
        and not word_is_complete(word, guessed_letters)
    ):

        print()
        print("Word:", create_display(word, guessed_letters))

        guesses_left = MAX_WRONG_GUESSES - wrong_guesses
        print("Wrong guesses remaining:", guesses_left)

        guess = input("Enter one letter: ").strip().lower()

        # Make sure the user enters exactly one letter.
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        # Do not count the same guess twice.
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Check whether the guessed letter is in the word.
        if process_guess(word, guess, guessed_letters):
            print("Correct!")
        else:
            wrong_guesses += 1
            print("Incorrect.")

    print()

    # Display the correct ending message.
    if word_is_complete(word, guessed_letters):
        print("Congratulations!")
        print("You guessed the word:", word)
    else:
        print("You are out of attempts.")
        print("The word was:", word)


if __name__ == "__main__":
    play_game()
