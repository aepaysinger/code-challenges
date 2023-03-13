from code_challenges.code_wars.pairs_of_shoes import make_pairs, find_pairs


def test_make_pairs():
    actual = make_pairs([[0, 23], [1, 21], [1, 23], [0, 21], [1, 22], [0, 22]])
    expected = {23: {0: 1, 1: 1}, 21: {0: 1, 1: 1}, 22: {0: 1, 1: 1}}

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_pairs():
    actual = find_pairs([[0, 21], [1, 23], [1, 21], [1, 23]])
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_pairs_false():
    actual = find_pairs([[0, 23], [1, 23], [1, 23], [0, 23], [0, 23], [0, 23]])
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_pairs_true():
    actual = find_pairs([[0, 23], [1, 23], [1, 23], [0, 23]])
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"
