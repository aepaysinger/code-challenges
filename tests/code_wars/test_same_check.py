from code_challenges.code_wars.same_check import comp


def test_comp_a():
    actual = comp(
        [121, 144, 19, 161, 19, 144, 19, 11],
        [121, 14641, 20736, 361, 25921, 361, 20736, 361],
    )
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_comp_b():
    actual = comp([], None)
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_comp_c():
    actual = comp([121, 144, 19, 161, 19, 144, 19, 11], [])
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_comp_d():
    actual = comp(
        [121, 144, 19, 161, 11, 144, 19, 11],
        [121, 14641, 20736, 361, 25921, 361, 20736, 361],
    )
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}."
