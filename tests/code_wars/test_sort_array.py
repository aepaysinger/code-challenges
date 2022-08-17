from code_challenges.code_wars.sort_array import sort_array


def test_sort_array():
    actual = sort_array([5, 8, 6, 3, 4])
    expected = [3, 8, 6, 5, 4]

    assert actual == expected, f"Should have returned {expected} but returned {actual}"


def test_sort_array_all_even():
    actual = sort_array([4, 6, 2, 54, 8, 10])
    expected = [4, 6, 2, 54, 8, 10]

    assert (
        actual == expected
    ), f"Nothing should change. You should returned {expected} but returned {actual}"


def test_sort_array_all_odd():
    actual = sort_array([1, 3, 77, 15, 53, 9])
    expected = [1, 3, 9, 15, 53, 77]

    assert (
        actual == expected
    ), f"Whole list shoud be sorted, should have returned {expected} but returned {actual}"
