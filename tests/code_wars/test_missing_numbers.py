from code_challenges.code_wars.missing_numbers import (
    MissingNumbers,
    find_missing_numbers,
)


def test_organize():
    missing_numbers = MissingNumbers([7, 1, 12, 9, 11, 14, 13, 6, 10, 5])

    assert missing_numbers.organize() == ([1, 5, 6, 7, 9, 10, 11, 12, 13, 14], 14)


def test_fill_in_the_gaps():
    missing_numbers = MissingNumbers([7, 1, 12, 9, 11, 14, 13, 6, 10, 5])
    missing_numbers.organize()

    assert missing_numbers.fill_in_the_gaps() == [2, 3, 4, 8]


def test_find_missing_numbers():
    actual = find_missing_numbers([8, 10, 11, 7, 3, 15, 6, 1, 14, 5, 12])
    expected = [2, 4, 9, 13]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_missing_numbers_no_one():
    actual = find_missing_numbers([8, 2, 6, 5, 7, 3, 4, 9])
    expected = [1]

    assert actual == expected, f"Returned {actual} instead of {expected}"
