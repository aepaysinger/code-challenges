from code_challenges.code_wars.rotate_text import rotate


def test_rotate_hello():
    actual = rotate("Hello")
    expected = ["elloH", "lloHe", "loHel", "oHell", "Hello"]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_rotate_123():
    actual = rotate("123")
    expected = ["231", "312", "123"]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_rotate():
    actual = rotate("")
    expected = []

    assert actual == expected, f"Returned {actual} instead of {expected}"
