from code_challenges.code_wars.snail import snail


def test_snail_3_x_3():
    actual = snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_snail_4_x_4():
    actual = snail([[1, 2, 3, 9], [4, 5, 6, 8], [7, 8, 9, 4], [7, 3, 6, 0]])
    expected = [1, 2, 3, 9, 8, 4, 0, 6, 3, 7, 7, 4, 5, 6, 9, 8]

    assert actual == expected, f"Returned {actual} instead of {expected}"
