from code_challenges.code_wars.make_the_deadfish_swim import parse


def test_parse():
    actual = parse("iiisdoso")
    expected = [8, 64]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_parse_different_characters():
    actual = parse("abcefg")
    expected = []

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_parse_both_characters():
    actual = parse("iciiobididobbhi")
    expected = [3, 3]

    assert actual == expected, f"Returned {actual} instead of {expected}"
