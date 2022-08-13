from code_challenges.code_wars.make_negative import make_negative


def test_make_negative_postive():
    actual = make_negative(5)
    expected = -5

    assert actual == expected, f"{actual} should return the same number but negative."


def test_make_negative_negative():
    actual = make_negative(-4)
    expected = -4

    assert actual == expected, "nothing changes because it is already negative"


def test_make_negative_zero():
    actual = make_negative(0)
    expected = 0

    assert actual == expected, "0 can't be made negative"
