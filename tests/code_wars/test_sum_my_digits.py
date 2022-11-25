from code_challenges.code_wars.sum_my_digits import sum_my_digits


def test_sum_my_digits_a():
    actual = sum_my_digits(10, [2, 1, 3], 6)
    expected = 10

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_sum_my_digits_b():
    actual = sum_my_digits(10, [2, 2, 5, 8], 6)
    expected = 11

    assert actual == expected, f"Returned {actual} instead of {expected}"
