from unittest.mock import patch
from code_challenges.advent_of_code.sonar_sweep import (
    find_depth_increase,
    find_depth_increase_window,
)


@patch("code_challenges.advent_of_code.sonar_sweep.get_sonar_map")
def test_find_depth_increase(get_sonar_map_mock):
    get_sonar_map_mock.return_value = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    actual = find_depth_increase()
    expected = 7

    assert actual == expected, f"Returned {actual} instrad of {expected}"


@patch("code_challenges.advent_of_code.sonar_sweep.get_sonar_map")
def test_find_depth_increase_window(get_sonar_map_mock):
    get_sonar_map_mock.return_value = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    actual = find_depth_increase_window()
    expected = 5

    assert actual == expected, f"Returned {actual} instrad of {expected}"
