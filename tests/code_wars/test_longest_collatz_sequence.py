from code_challenges.code_wars.longest_collatz_sequence import (
    collatz_number,
    find_collatz_sequence,
    find_longest_length,
)


def test_collatz_number_eveb():
    actual = collatz_number(4)
    expected = 2.0

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_collatz_number_odd():
    actual = collatz_number(5)
    expected = 16

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_collatz_sequence():
    actual = find_collatz_sequence([2, 4, 3])
    expected = {2: 1, 4: 2, 3: 7}

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_longest_length():
    actual = find_longest_length([2, 4, 3])
    expected = 3

    assert actual == expected, f"Returned {actual} instead of {expected}"
