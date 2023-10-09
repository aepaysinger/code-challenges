from code_challenges.code_wars.amount_of_sets import find_amount_of_sets


def test_find_amount_of_sets_a():
    actual = find_amount_of_sets(["A", "B", "C"])
    expected = 7

    assert actual == expected, f"Retyurned {actual} instead of {expected}"


def test_find_amount_of_sets_b():
    actual = find_amount_of_sets([1, 2, 3, 4, 1])
    expected = 15

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_amount_of_sets_c():
    actual = find_amount_of_sets([])
    expected = 0

    assert actual == expected, f"Returned {actual} instead of {expected}"
