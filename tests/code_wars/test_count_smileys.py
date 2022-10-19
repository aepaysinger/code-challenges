from code_challenges.code_wars.count_smileys import count_smileys


def test_count_smileys_all():
    actual = count_smileys([":D", ":~)", ";~D", ":)"])
    expected = 4

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_count_smileys_some():
    actual = count_smileys([":)", ":(", ":D", ":O", ":;"])
    expected = 2

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_count_smileys_none():
    actual = count_smileys([";(", ":>", ":}", ":]"])
    expected = 0

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_count_smileys_too_long():
    actual = count_smileys([";(", ":--)", ":)", ":]"])
    expected = 1

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_count_smileys_wrong_eyes():
    actual = count_smileys(["*)", "^--)", "|)", "?]"])
    expected = 0

    assert actual == expected, f"Returned {actual} instead of {expected}"
