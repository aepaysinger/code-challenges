from code_challenges.code_wars.split_strings import split_the_string


def test_split_the_string_even_string_len():
    actual = split_the_string("ijsnytfg")
    expected = ["ij", "sn", "yt", "fg"]

    assert (
        actual == expected
    ), "you should return a list with the strings evenly split into pairs."


def test_split_the_string_odd():
    actual = split_the_string("bhystfo")
    expected = ["bh", "ys", "tf", "o_"]

    assert (
        actual == expected
    ), "When the string is uneven th last pair in the group needs a _ added to it."
