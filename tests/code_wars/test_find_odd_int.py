from code_challenges.code_wars.find_odd_int import finding_odd_int


def test_finding_odd_int():
    actual = finding_odd_int([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1])
    expected = 10

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_odd_int_a():
    actual = finding_odd_int([1, 2, 1, 3, 1, 3, 10, 1, 2, 1, 1])
    expected = 10

    assert actual == expected, f"Returned {actual} instead of {expected}"
