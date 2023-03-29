from code_challenges.code_wars.translating import to_nato


def test_to_nato_a():
    actual = to_nato("Did not see that coming")
    expected = "Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_to_nato_b():
    actual = to_nato(".d?d!")
    expected = ". Delta ? Delta !"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_to_nato_c():
    actual = to_nato("If, you can read?")
    expected = "India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?"

    assert actual == expected, f"Returned {actual} instead of {expected}"
