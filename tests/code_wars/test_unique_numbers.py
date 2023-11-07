from code_challenges.code_wars.unique_number import UniqueNumber, find_unique_number


def test_unique_number():
    numbers = UniqueNumber([1, 1, 1, 2, 1, 1])

    assert numbers.find_unique() == 2


def test_find_unique_number():
    actual = find_unique_number([1, 2, 3, 1, 2, 1, 4, 3, 2])
    expected = 4

    assert actual == expected, f"Returned {actual} instead of {expected}"
