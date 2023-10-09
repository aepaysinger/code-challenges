import pytest


from code_challenges.code_wars.luck_check import luck_check


def test_luck_check_true():
    actual = luck_check("683179")
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_luck_check_false():
    actual = luck_check("683000")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_luck_check_odd_length():
    actual = luck_check("6838179")
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_luck_check_empty_string():
    with pytest.raises(ValueError) as exc_info:
        luck_check("")
    assert exc_info.value.args[0] == "empty string"


def test_luck_check_letters():
    with pytest.raises(ValueError) as exc_info:
        luck_check("234jh43j2")
    assert exc_info.value.args[0] == "needs to be numbers"
