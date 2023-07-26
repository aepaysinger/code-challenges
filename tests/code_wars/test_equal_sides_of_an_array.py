from code_challenges.code_wars.equal_sides_of_an_array import (
    EqualSumSidesArray,
    find_even_index,
)


def test_sum_sides_of_array():
    equal_sides = EqualSumSidesArray([10, -80, 10, 10, 15, 35])

    assert equal_sides.sum_sides_of_array() == -1


def test_find_even_index_0():
    actual = find_even_index([6, 4, -2, 8, -10])
    expected = 0

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_even_index_0_at_0():
    actual = find_even_index([0, 6])
    expected = 1

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_even_index():
    actual = find_even_index([0, 10, -80, 10, 10, 15, 35, 20])
    expected = 7

    assert actual == expected, f"Returned {actual} instead of {expected}"
