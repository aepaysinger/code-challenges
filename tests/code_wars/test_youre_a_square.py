from code_challenges.code_wars.youre_a_square import is_square


def test_youre_a_square_false():
    actual = is_square(34)
    expected = False

    assert actual == expected, f"Returned {actual}, instead of {expected}"


def test_youre_a_square_true():
    actual = is_square(25)
    expected = True

    assert actual == expected, f"Returned {actual}, instead of {expected}"