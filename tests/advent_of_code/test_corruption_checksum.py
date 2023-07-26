from unittest.mock import patch


from code_challenges.advent_of_code.corruption_checksum import (
    checksum,
    evenly_divisible_values,
)


@patch("code_challenges.advent_of_code.corruption_checksum.spreadsheet_input")
def test_checksum_a(spreadsheet_input_mock):
    spreadsheet_input_mock.return_value = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
    actual = checksum()
    expected = 18

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.corruption_checksum.spreadsheet_input")
def test_evenly_divisibile_values_a(spreadsheet_input_mock):
    spreadsheet_input_mock.return_value = [[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]
    actual = evenly_divisible_values()
    expected = 9

    assert actual == expected, f"Returned {actual} instead of {expected}"
