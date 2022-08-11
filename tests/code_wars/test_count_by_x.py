from code_challenges.code_wars.count_by_x import count_by


def test_count_by_2():
    actual = count_by(2, 5)
    expected = "2, 4, 6, 8, 10"

    assert actual == expected, f"should have returned {expected}, but returned {actual}"


def test_count_by_5():
    actual = count_by(5, 6)
    expected = "5, 10, 15, 20, 25, 30"

    assert actual == expected, f"should have returned {expected}, but returned {actual}"

