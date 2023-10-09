from code_challenges.code_wars.phone_text import presses


def test_presses_a():
    actual = presses("abcDEFghiJKLmnoPQRstuVWXyz")
    expected = 56

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_presses_b():
    actual = presses("1234567890")
    expected = 37

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_presses_c():
    actual = presses("the * look amazing")
    expected = 33

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_presses_d():
    actual = presses("her dog weighs 50#s")
    expected = 39

    assert actual == expected, f"Returned {actual} instead of {expected}"
