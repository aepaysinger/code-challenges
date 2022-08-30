from code_challenges.code_wars.highest_scoring_word import high


def test_high():
    actual = high("it will take a string")
    expected = "string"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_high_nultiple_same_score():
    actual = high("ade j ee gc")
    expected = "ade j ee gc"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_high():
    actual = high("not sure what other test to run")
    expected = "other"

    assert actual == expected, f"Returned {actual} instead of {expected}"
