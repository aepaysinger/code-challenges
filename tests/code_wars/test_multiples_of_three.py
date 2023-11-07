from code_challenges.code_wars.multiples_of_three import find_mult_3


def test_find_mult_3_a():
    actual = find_mult_3(362)
    expected = [4, 63]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_mult_3_b():
    actual = find_mult_3(6063)
    expected = [25, 6630]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_mult_3_c():
    actual = find_mult_3(7766553322)
    expected = [55510, 766553322]

    assert actual == expected, f"Returned {actual} instead of {expected}"
