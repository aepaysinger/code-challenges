from code_challenges.code_wars.lonliest_character import loneliest


def test_lonliest_a():
    actual = loneliest("abc d   ef  g   h i j      ")
    expected = ["g"]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_lonliest_b():
    actual = loneliest("abc")
    expected = ["a", "b", "c"]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_lonliest_c():
    actual = loneliest("a  b  c  de  ")
    expected = ["b", "c"]

    assert actual == expected, f"Returned {actual} instead of {expected}"
