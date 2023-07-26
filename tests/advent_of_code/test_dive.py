from unittest.mock import patch

from code_challenges.advent_of_code.dive import find_depth, find_depth_with_aim


@patch("code_challenges.advent_of_code.dive.get_directions")
def test_find_depth(get_directions_mock):
    get_directions_mock.return_value = [
        ["forward", "5"],
        ["down", "5"],
        ["forward", "8"],
        ["up", "3"],
        ["down", "8"],
        ["forward", "2"],
    ]
    actual = find_depth()
    expected = 150

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.dive.get_directions")
def test_find_depth_with_aim(get_directions_mock):
    get_directions_mock.return_value = [
        ["forward", "5"],
        ["down", "5"],
        ["forward", "8"],
        ["up", "3"],
        ["down", "8"],
        ["forward", "2"],
    ]
    actual = find_depth_with_aim()
    expected = 900

    assert actual == expected, f"Returned {actual} instead of {expected}"
