from code_challenges.code_wars.two_sum import two_sum


def test_two_sum_a():
    actual = two_sum([1, 2, 3], 4)
    expected = [0, 2]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_two_sum_b():
    actual = two_sum([1234, 5678, 9012], 14690)
    expected = [1, 2]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_two_sum_c():
    actual = two_sum([2, 2, 3], 4)
    expected = [0, 1]

    assert actual == expected, f"Returned {actual} instead of {expected}"
