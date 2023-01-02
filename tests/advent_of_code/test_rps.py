from unittest.mock import patch


from code_challenges.advent_of_code.rps import rps


@patch("code_challenges.advent_of_code.rps.get_rps_moves")
def test_rps_a(get_rps_moves_mock):
    get_rps_moves_mock.return_value = ["B X", "B Y", "A Y", "B Y"]
    actual = rps()
    expected = 15

    assert actual == expected


@patch("code_challenges.advent_of_code.rps.get_rps_moves")
def test_rps_b(get_rps_moves_mock):
    get_rps_moves_mock.return_value = [
        "A Y",
        "A Y",
        "B X",
        "B Y",
        "B X",
        "B Y",
        "C X",
        "A Y",
        "A X",
        "A Z",
        "A Y",
        "B Z",
        "C Y",
        "C X",
        "B Y",
        "B Z",
        "A Y",
        "B Y",
        "B Z",
        "A Y",
        "A Y",
        "B Y",
        "B Z",
        "B Y",
        "A Y",
    ]
    actual = rps()
    expected = 121

    assert actual == expected


@patch("code_challenges.advent_of_code.rps.get_rps_moves")
def test_rps_c(get_rps_moves_mock):
    get_rps_moves_mock.return_value = [
        "B Z",
        "C X",
        "A Y",
        "A Y",
        "B Y",
        "B Z",
        "C X",
        "A X",
        "A Y",
    ]
    actual = rps()
    expected = 42

    assert actual == expected
