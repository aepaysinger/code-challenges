from unittest.mock import patch

from code_challenges.advent_of_code.lanternfish import (
    count_lanternfish_growth_attempA,
    count_lanternfish_growth,
)


@patch("code_challenges.advent_of_code.lanternfish.get_lanternfish")
def test_count_lanterfish_growth_attemptA(mock_get_lanternfish):
    mock_get_lanternfish.return_value = [3, 4, 3, 1, 2]
    actual = count_lanternfish_growth_attempA(18)
    expected = 26

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.lanternfish.get_lanternfish")
def test_count_lanterfish_growth(mock_get_lanternfish):
    mock_get_lanternfish.return_value = [3, 4, 3, 1, 2]
    actual = count_lanternfish_growth(80)
    expected = 5934

    assert actual == expected, f"Returned {actual} instead of {expected}"
