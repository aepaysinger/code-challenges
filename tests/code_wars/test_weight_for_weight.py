from code_challenges.code_wars.weight_for_weight import weight_for_weight


def test_weight_for_weight_a():
    actual = weight_for_weight("103 123 4444 99 2000")
    expected = "2000 103 123 4444 99"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_weight_for_weight_b():
    actual = weight_for_weight("2000 10003 1234000 44444444 9999 11 11 22 123")
    expected = "11 11 2000 10003 22 123 1234000 44444444 9999"

    assert actual == expected, f"Returned {actual} instead of {expected}"
