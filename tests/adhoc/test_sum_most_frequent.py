from code_challenges.adhoc.sum_most_frequent import sum_most_frequent_numbers


def test_sum_most_frequent_numbers():
    actual = sum_most_frequent_numbers([1, 4, 3, 3, 7, 2, 2, 9])
    expected = 5

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_sum_most_frequent_numbers_smallest_first():
    actual = sum_most_frequent_numbers([1, 1, 1, 1, 2, 2])
    expected = 3

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_sum_most_frequent_numbers_more_then_2_same_length():
    actual = sum_most_frequent_numbers([1, 1, 7, 8, 8, 4, 3, 3])
    expected = 11

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_sum_most_frequent_numbers_different_lengths():
    actual = sum_most_frequent_numbers([8, 8, 1, 1, 1, 6, 6, 6, 6])
    expected = 7

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_sum_most_frequent_numbers_mixed_up():
    actual = sum_most_frequent_numbers([1, 5, 2, 1, 7, 8, 3, 1, 5, 5, 2])
    expected = 6

    assert actual == expected, f"Returned {actual} instead of {expected}"
