from unittest.mock import patch

from code_challenges.advent_of_code.chronal_calibration import (
    find_final_frequency,
    visited_frequency_twice,
)


@patch("code_challenges.advent_of_code.chronal_calibration.frequency_input")
def test_find_final_frequency(mock_frequency_input):
    mock_frequency_input.return_value = ["+3", "+3 ", "+4", "-2", "-4"]
    actual = find_final_frequency()
    expected = 4

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.chronal_calibration.frequency_input")
def test_visited_frequency_twice(mock_frequency_input):
    mock_frequency_input.return_value = ["+3", "+3 ", "+4", "-2", "-4"]
    actual = visited_frequency_twice()
    expected = 10

    assert actual == expected, f"Returned {actual} instead of {expected}"
