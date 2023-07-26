from code_challenges.code_wars.anagram_difference import anagram_difference


def test_anagram_difference1():
    actual = anagram_difference("codewars", "hackerrank")
    expected = 10

    assert actual == expected, f"Returned {actual} instrad of {expected}"


def test_anagram_difference2():
    actual = anagram_difference("hello", "world")
    expected = 6

    assert actual == expected, f"Returned {actual} instead of {expected}"
