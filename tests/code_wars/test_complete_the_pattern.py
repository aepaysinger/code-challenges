from code_challenges.code_wars.complete_the_pattern import pattern


def test_pattern_a():
    actual = pattern(-9)
    expected = ""

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_pattern_b():
    actual = pattern(5)
    expected = "55555\n54444\n54333\n54322\n54321"

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_pattern_c():
    actual = pattern(0)
    expected = ""

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_pattern_d():
    actual = pattern(12)
    expected = "222222222222\n211111111111\n210000000000\n210999999999\n210988888888\n210987777777\n210987666666\n210987655555\n210987654444\n210987654333\n210987654322\n210987654321"

    assert actual == expected, f"Returned {actual} instead of {expected}."
