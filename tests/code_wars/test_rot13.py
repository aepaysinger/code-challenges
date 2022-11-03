from code_challenges.code_wars.rot13 import rot13


def test_rot13_lower():
    actual = rot13("test")
    expected = "grfg"

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_rot13_upper():
    actual = rot13("TEST")
    expected = "GRFG"

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_rot13_num():
    actual = rot13("1a2b3c")
    expected = "1n2o3p"

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_rot13_mix():
    actual = rot13("1A2b3C")
    expected = "1N2o3P"

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_rot13_special():
    actual = rot13("test$*-TEST")
    expected = "grfg$*-GRFG"

    assert actual == expected, f"Returned {actual} instead of {expected}."
