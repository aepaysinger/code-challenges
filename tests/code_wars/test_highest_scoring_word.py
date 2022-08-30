from code_challenges.code_wars.highest_scoring_word import highest_scoring_word


def test_highest_scoring_word_1():
    actual = high("it will take a string")
    expected = "string"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_highest_scoring_word_multiple_same_score():
    actual = high("ade j ee gc")
    expected = "ade j ee gc"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_highest_scoring_word_b():
    actual = high("not sure what other test to run")
    expected = "other"

    assert actual == expected, f"Returned {actual} instead of {expected}"
