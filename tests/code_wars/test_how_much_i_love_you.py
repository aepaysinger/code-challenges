from code_challenges.code_wars.how_much_i_love_you import how_much_i_love_you


def test_how_much_i_love_you_1():
    actual = how_much_i_love_you(19)
    expected = "I love you"

    assert actual == expected, "19 % 6 = 1"


def test_how_much_i_love_you_2():
    actual = how_much_i_love_you(458)
    expected = "a little"

    assert actual == expected, "458 % 6 = 2"


def test_how_much_i_love_you_3():
    actual = how_much_i_love_you(279)
    expected = "a lot"

    assert actual == expected, "279 % 6 = 3"


def test_how_much_i_love_you_4():
    actual = how_much_i_love_you(148)
    expected = "passionately"

    assert actual == expected, "148 % 6 = 4"


def test_how_much_i_love_you_5():
    actual = how_much_i_love_you(587)
    expected = "madly"

    assert actual == expected, "587 % 6 = 5"


def test_how_much_i_love_you_6():
    actual = how_much_i_love_you(66)
    expected = "not at all"

    assert actual == expected, "66 % 6 = 0"
