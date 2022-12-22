from code_challenges.code_wars.facebook_likes import LikesAmount, likes


def test_likes_0():
    actual = likes([])
    expected = "no one likes this"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_likes_1():
    actual = likes(["April"])
    expected = "April likes this"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_likes_2():
    actual = likes(["April", "Max"])
    expected = "April and Max like this"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_likes_3():
    actual = likes(["April", "Max", "Pedro"])
    expected = "April, Max and Pedro like this"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_likes_4():
    actual = likes(["April", "Max", "Pedro", "Stefanie"])
    expected = "April, Max and 2 others like this"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_likes_5():
    actual = likes(["April", "Max", "Pedro", "Stefanie", "Sandra"])
    expected = "April, Max and 3 others like this"

    assert actual == expected, f"Returned {actual} instead of {expected}"
