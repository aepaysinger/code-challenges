from code_challenges.advent_of_code.md5 import crack_the_code_lowest


def test_crack_the_code_lowest_abcdef3():
    actual = crack_the_code_lowest("abcdef", 3)
    expected = 3337

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_crack_the_code_lowest_abcdef4():
    actual = crack_the_code_lowest("abcdef", 4)
    expected = 31556

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_crack_the_code_lowest_abcdef5():
    actual = crack_the_code_lowest("abcdef", 5)
    expected = 609043

    assert actual == expected, f"Returned {actual} instead of {expected}"
