from code_challenges.adhoc.sum_of_the_smallest import sum_of_the_smallest


def test_sum_of_the_smallest():
    actual = sum_of_the_smallest([5, 1, 7, 9, 3, 2])
    expected = 3

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_sum_of_the_smallest_with_negative():
    actual = sum_of_the_smallest([5, 1, -8, 9, 3, 2])
    expected = 3

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_sum_of_the_smallest_multiple_same():
    actual = sum_of_the_smallest([5, 1, 1, 9, 3, 2])
    expected = 2

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_sum_of_the_smallest_multiple_same():
    actual = sum_of_the_smallest([-5, -1, -1, -9, -3, -2])
    expected = None

    assert actual == expected, f"Returned {actual} instead of {expected}"