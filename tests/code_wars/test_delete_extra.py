from code_challenges.code_wars.delete_extra import delete_extra


def test_delete_extra_2():
    actual = delete_extra([1, 2, 3, 1, 2, 1, 2, 3], 2)
    expected = [1, 2, 3, 1, 2, 3]

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_delete_extra_4():
    actual = delete_extra([1, 2, 3, 1, 2, 1, 2, 3], 4)
    expected = [1, 2, 3, 1, 2, 1, 2, 3]

    assert actual == expected, f"Returned {actual} instead of {expected}."
