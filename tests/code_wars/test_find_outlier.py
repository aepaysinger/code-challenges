from code_challenges.code_wars.find_outlier import find_outlier


def test_find_outlier_odd():
    actual = find_outlier([4, 98, 36, 71, 88, 102])
    expected = 71

    assert (
        actual == expected
    ), f"You should have returned the odd number {expected}, but returned {actual}"


def test_find_outlier_even():
    actual = find_outlier([1, 63, 75, 88, 1001, 47])
    expected = 88

    assert (
        actual == expected
    ), f"You should have returned the even number {expected}, but returned {actual}"
