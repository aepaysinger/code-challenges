from code_challenges.hacker_rank.find_string import FindString, find_string


def test_find_string_a():
    actual = find_string("ABCDCDCYHCDA", "CDC")
    expected = 2

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_string_b():
    actual = find_string("ABCDCdCYHCDA", "CDC")
    expected = 1

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_hidden_characters():
    find_string = FindString("Try this out", "THIS")

    assert find_string.find_hidden_characters() == 0
