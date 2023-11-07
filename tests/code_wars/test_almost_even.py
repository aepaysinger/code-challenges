from code_challenges.code_wars.almost_even import split_integer


def test_split_integer_a():
    actual = split_integer(20, 5)
    expected = [4, 4, 4, 4, 4]

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_split_intege_b():
    actual = split_integer(20, 6)
    expected = [3, 3, 3, 3, 4, 4]

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_split_integer_c():
    actual = split_integer(10, 1)
    expected = [10]

    assert actual == expected, f"Returned {actual} instead of {expected}."
