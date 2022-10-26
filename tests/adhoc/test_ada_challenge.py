from code_challenges.adhoc.ada_challenge import bubble_tea_calculator


def test_ada_challenge_A():
    actual = bubble_tea_calculator("milk", ["boba", "jelly", "taro"], False)
    expected = "The cost is $6.50"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_ada_challenge_B():
    actual = bubble_tea_calculator("rose", [], False)
    expected = "The cost is $5.85"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_ada_challenge_C():
    actual = bubble_tea_calculator("oolong", ["chia"], True)
    expected = "The cost is $3.95"

    assert actual == expected, f"Returned {actual} instead of {expected}"