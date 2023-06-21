from code_challenges.code_wars.multiples_of_3_and_5 import multiples_of_3_and_5


def test_multiples_of_3_and_5_even_number():
    actual = multiples_of_3_and_5(20)
    expected = 78

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_multiples_of_3_and_5_odd_number():
    actual = multiples_of_3_and_5(7)
    expected = 14

    assert actual == expected, f"Returned {actual} instead of {expected}"
