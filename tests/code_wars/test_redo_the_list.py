from code_challenges.code_wars.redo_the_list import arrange


def test_arrange():
    actual = arrange([1, 2, 3, 4, 5, 6])
    expected = [1, 6, 5, 2, 3, 4]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_arrange_odd_length():
    actual = arrange([1, 2, 3, 4, 5])
    expected = [1, 5, 4, 2, 3]

    assert actual == expected, f"Returned {actual} instead of {expected}"
