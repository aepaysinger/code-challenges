from code_challenges.code_wars.find_next_item import cycle


def test_cycle_a():
    actual = cycle(1, [4, 7, 5, 6, 1], 5)
    expected = 6

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_cycle_b():
    actual = cycle(1, [4, 7, 5, 6, 1], 1)
    expected = 4

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_cycle_c():
    actual = cycle(1, [4, 7, 5, 5, 6, 1], 5)
    expected = 5

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_cycle_d():
    actual = cycle(-1, [5, 7, 8, 2, 4, 3, 5], 2)
    expected = 8

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_cycle_e():
    actual = cycle(-1, [5, 7, 8, 2, 4, 3, 9], 5)
    expected = 9

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_cycle_f():
    actual = cycle(-1, [5, 7, 8, 2, 4, 3, 9], 1)
    expected = None

    assert actual == expected, f"Returned {actual} instead of {expected}"