from code_challenges.hacker_rank.the_captains_room import find_the_captain


def test_find_the_captain():
    actual = find_the_captain(
        "1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2".split(" ")
    )
    expected = "8"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_the_captain_no_captain():
    actual = find_the_captain("3 5 7 4 5 3 7 4 5 5".split(" "))
    expected = "where did the captain go?"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_the_captain_and_crew():
    actual = find_the_captain(
        "1 2 3 6 5 9 4 2 5 3 6 1 6 1 4 3 6 8 4 3 1 5 6 2".split(" ")
    )
    expected = "Don't forget the crew!"

    assert actual == expected, f"Returned {actual} instead of {expected}"
