from code_challenges.code_wars.find_odd_int import FindOddInt
from code_challenges.code_wars.find_odd_int import finding_odd_int


def test_finding_odd_int():
    actual = finding_odd_int([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1])
    expected = 10

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_finding_odd_int_a():
    actual = finding_odd_int([1, 2, 1, 3, 1, 3, 10, 1, 2, 1, 1])
    expected = 10

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_odd_int_set_numbers_amount():
    find_odd = FindOddInt([1, 2, 3, 4, 1, 2, 3])
    find_odd.set_numbers_amount()

    assert find_odd.numbers_amount == {1: 2, 2: 2, 3: 2, 4: 1}


def test_find_odd_int():
    find_odd = FindOddInt([1, 1, 1, 1, 2, 2, 6, 6, 6, 9, 9])
    find_odd.set_numbers_amount()

    assert find_odd.find_odd_int() == 6
