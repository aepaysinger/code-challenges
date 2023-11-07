from code_challenges.code_wars.palindromic_numbers import palindromize


def test_palindromize_a():
    actual = palindromize(195)
    expected = "4 9339"

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_palindromize_b():
    actual = palindromize(265)
    expected = "5 45254"

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_palindromize_c():
    actual = palindromize(28)
    expected = "2 121"

    assert actual == expected, f"Returned {actual} instead of {expected}."
