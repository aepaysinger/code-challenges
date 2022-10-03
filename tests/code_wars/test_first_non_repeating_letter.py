from code_challenges.code_wars.first_non_repeating_letter import (
    first_non_repeating_letter,
)


def test_first_non_repeating_letter():
    actual = first_non_repeating_letter("stress")
    expected = "t"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_first_non_repeating_letter_middle():
    actual = first_non_repeating_letter("missisqsippm")
    expected = "q"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_first_non_repeating_letter_last():
    actual = first_non_repeating_letter("abcdabcde")
    expected = "e"

    assert actual == expected, f"Returned {actual} instead of {expected}"
