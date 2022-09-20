from code_challenges.code_wars.scramble import scramble, unscramble


def test_scramble_true():
    actual = scramble("rkqodlw", "world")
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_scramble_false():
    actual = scramble("abcdefg", "world")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"
