from code_challenges.code_wars.football_cards import football_cards


def test_football_cards():
    actual = football_cards(["A4Y", "A4Y"])
    expected = (10,11)

    assert actual == expected, f"Returned {actual} instead of {expected}"