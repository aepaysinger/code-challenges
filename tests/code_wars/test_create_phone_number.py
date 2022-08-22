from code_challenges.code_wars.create_phone_number import create_phone_number


def test_create_phone_number():
    actual = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    expected = "(123) 456-7890"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_create_phone_number_too_long():
    actual = create_phone_number([3, 5, 8, 3, 9, 4, 6, 1, 0, 2, 4, 7])
    expected = "(358) 394-6102 (these were extra 47)"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_create_phone_number_too_short():
    actual = create_phone_number([3, 6, 3, 8, 9, 3, 5, 6])
    expected = "You don't have enought numbers"

    assert actual == expected, f"Returned {actual} instead of {expected}"
