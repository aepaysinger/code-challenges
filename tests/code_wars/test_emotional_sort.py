from code_challenges.code_wars.emotional_sort import sort_emotions


def test_sort_emotions_true():
    actual = sort_emotions(["T_T", ":D", ":(", ":("], True)
    expected = [":D", ":(", ":(", "T_T"]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_sort_emotions_false():
    actual = sort_emotions([":)", "T_T", ":)", ":D", ":D"], False)
    expected = ["T_T", ":)", ":)", ":D", ":D"]

    assert actual == expected, f"Returned {actual} instead of {expected}"
