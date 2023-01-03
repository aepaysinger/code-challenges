from code_challenges.code_wars.backspace_string import Backspace, backspace_string


def test_backsapce():
    the_string = Backspace("abc#d##c")

    assert the_string.hit_backspace() == "ac"


def test_backspace_string():
    actual = backspace_string("abc####d##c#")
    expected = ""

    assert actual == expected, f"Returned {actual} instead of {expected}"
