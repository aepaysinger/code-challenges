from unittest.mock import patch

from code_challenges.advent_of_code.treachery_of_whales import (
    fuel_spent_to_align_position,
    fuel_spent_to_align_position_part2,
    find_fuel_total,
)


@patch("code_challenges.advent_of_code.treachery_of_whales.get_crab_positions")
def test_fuel_spent_to_align_position(mock_get_crab_positions):
    mock_get_crab_positions.return_value = [0, 1, 1, 2, 2, 2, 4, 7, 14, 16]
    actual = fuel_spent_to_align_position()
    expected = 37

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.treachery_of_whales.get_crab_positions")
def test_fuel_spent_to_align_position_part2(mock_get_crab_positions):
    mock_get_crab_positions.return_value = [0, 1, 1, 2, 2, 2, 4, 7, 14, 16]
    actual = fuel_spent_to_align_position_part2()
    expected = 168

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.treachery_of_whales.get_crab_positions")
def test_fuel_spent_to_align_position_part2_b(mock_get_crab_positions):
    mock_get_crab_positions.return_value = [0, 1, 1, 2, 2, 4, 5, 7, 14, 16]
    actual = fuel_spent_to_align_position_part2()
    expected = 162

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_fuel_total():
    actual = find_fuel_total([0, 1, 1, 2, 2, 2, 4, 7, 14, 16], 2)
    expected = 206

    assert actual == expected, f"Returned {actual} instead of {expected}"
