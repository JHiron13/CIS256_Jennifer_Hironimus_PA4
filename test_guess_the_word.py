# Jennifer Hironimus
# CIS256 Fall 2026
# Programming Assignment 4

from guess_the_word import (
    WORDS,
    choose_word,
    create_display,
    process_guess,
    word_is_complete
)


# Test that the selected word comes from
# the predefined list of words.
def test_choose_word_from_list():
    selected_word = choose_word()
    assert selected_word in WORDS


# Test that a correct guess is recognized.
def test_correct_guess():
    guessed_letters = set()

    result = process_guess(
        "python",
        "p",
        guessed_letters
    )

    assert result is True
    assert "p" in guessed_letters


# Test that an incorrect guess is recognized.
def test_incorrect_guess():
    guessed_letters = set()

    result = process_guess(
        "python",
        "z",
        guessed_letters
    )

    assert result is False
    assert "z" in guessed_letters


# Test that all repeated letters are revealed.
def test_repeated_letters_are_revealed():
    guessed_letters = {"e"}

    display = create_display(
        "letter",
        guessed_letters
    )

    assert display == "_ e _ _ e _"


# Test that the program recognizes
# when the entire word is complete.
def test_word_is_complete():
    guessed_letters = set("python")

    assert word_is_complete(
        "python",
        guessed_letters
    ) is True
