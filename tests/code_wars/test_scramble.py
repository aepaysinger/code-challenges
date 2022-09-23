from code_challenges.code_wars.scramble import count_characters, scramble


def test_count_characters():
    actual = count_characters("rkqodlw", "world")
    expected = {"r": 1, "k": 1, "q": 1, "o": 1, "d": 1, "l": 1, "w": 1}, {
        "w": 1,
        "o": 1,
        "r": 1,
        "l": 1,
        "d": 1,
    }

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_scramble_not_in_scrambled_counter():
    actual = scramble("abcdefg", "world")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_scramble_not_enough_characters():
    actual = scramble("pipesmiss", "mississippi")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_scramble_True():
    actual = scramble("evolve", "love")
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"
