from code_challenges.code_wars.football_cards import football_cards


def test_football_cards_2():
    actual = football_cards(["A4Y", "A4Y"])
    expected = (10, 11)

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_football_cards_4():
    actual = football_cards(["A4Y", "A5R", "B5R", "A4Y", "B6Y"])
    expected = (9, 10)

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_football_cards_early():
    actual = football_cards(["A4R", "A6R", "A8R", "A1R", "A3R", "B1R"])
    expected = (6, 11)

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_football_cards_double_digit_player():
    actual = football_cards(["A4R", "A10R", "B11R", "A1R", "A3R", "B1R"])
    expected = (7, 9)

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_football_cards_RY():
    actual = football_cards(["A4R", "A10R", "A4Y", "A1R", "A3R", "B1R"])
    expected = (7, 10)

    assert actual == expected, f"Returned {actual} instead of {expected}"
