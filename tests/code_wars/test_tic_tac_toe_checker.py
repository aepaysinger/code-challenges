from code_challenges.code_wars.tic_tac_toe_checker import find_winner


def test_find_winner_1():
    actual = find_winner([[2, 1, 2],
              [1, 1, 1],
              [2, 2, 1]])
    expected = 1

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_winner_2():
    actual = find_winner([[2, 1, 2],
              [0, 1, 2],
              [2, 2, 2]])
    expected = 2

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_winner_0():
    actual = find_winner([[2, 1, 2],
                          [1, 1, 2],
                          [2, 2, 1]])
    expected = 0

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_winner_neg1():
    actual = find_winner([[2, 1, 0],
              [0, 1, 2],
              [2, 0, 1]])
    expected = -1

    assert actual == expected, f"Returned {actual} instead of {expected}"