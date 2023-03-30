from code_challenges.adhoc.two_sum import two_sum


def test_two_sum_a():
    actual = two_sum([3, 2, 4], 6)
    expected = [1, 2]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_two_sum_b():
    actual = two_sum([3, 3, 1, 8, 7, 4], 6)
    expected = [0, 1]

    assert actual == expected, f"Returned {actual} instead of {expected}"
