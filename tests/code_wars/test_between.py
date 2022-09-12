from code_challenges.code_wars.between import between


def test_between_positive():
    actual = between(1, 6)
    expected = [1, 2, 3, 4, 5, 6]

    assert actual == expected, f"should have returned {expected} but returned {actual}"


def test_between_negatve():
    actual = between(-7, -3)
    expected = [-7, -6, -5, -4, -3]

    assert actual == expected, f"should have returned {expected} but returned {actual}"


def test_between_positive_and_negative():
    actual = between(-2, 2)
    expected = [-2, -1, 0, 1, 2]

    assert actual == expected, f"should have returned {expected} but returned {actual}"


def test_between_wrong_order():
    actual = between(4, 2)
    expected = "incorrect range, enter the smaller number first"

    assert actual == expected, f"should have returned {expected} but returned {actual}"
