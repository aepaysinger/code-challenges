from unittest.mock import patch

from code_challenges.advent_of_code.hydrothermal_venture import (
    mark_coordinates_horizontal_vertical,
    mark_coordinates_horizontal_vertical_diagonal,
    get_coordinate_pairs,
)


@patch("code_challenges.advent_of_code.hydrothermal_venture.get_vents_input")
def test_mark_coordinates_horizontal_vertical(mock_get_vents_input):
    mock_get_vents_input.return_value = [
        ["0", "9"],
        ["5", "9"],
        ["8", "0"],
        ["0", "8"],
        ["9", "4"],
        ["3", "4"],
        ["2", "2"],
        ["2", "1"],
        ["7", "0"],
        ["7", "4"],
        ["6", "4"],
        ["2", "0"],
        ["0", "9"],
        ["2", "9"],
        ["3", "4"],
        ["1", "4"],
        ["0", "0"],
        ["8", "8"],
        ["5", "5"],
        ["8", "2"],
    ]
    actual = mark_coordinates_horizontal_vertical()
    expected = 5

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.hydrothermal_venture.get_vents_input")
def test_mark_coordinates_horizontal_vertical_diagonal(mock_get_vents_input):
    mock_get_vents_input.return_value = [
        ["0", "9"],
        ["5", "9"],
        ["8", "0"],
        ["0", "8"],
        ["9", "4"],
        ["3", "4"],
        ["2", "2"],
        ["2", "1"],
        ["7", "0"],
        ["7", "4"],
        ["6", "4"],
        ["2", "0"],
        ["0", "9"],
        ["2", "9"],
        ["3", "4"],
        ["1", "4"],
        ["0", "0"],
        ["8", "8"],
        ["5", "5"],
        ["8", "2"],
    ]
    actual = mark_coordinates_horizontal_vertical_diagonal()
    expected = 12

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.hydrothermal_venture.get_vents_input")
def test_get_coordinate_pairs(mock_get_vents_input):
    mock_get_vents_input.return_value = [
        ["0", "9"],
        ["5", "9"],
        ["8", "0"],
        ["0", "8"],
        ["9", "4"],
        ["3", "4"],
        ["2", "2"],
        ["2", "1"],
        ["7", "0"],
        ["7", "4"],
        ["6", "4"],
        ["2", "0"],
        ["0", "9"],
        ["2", "9"],
        ["3", "4"],
        ["1", "4"],
        ["0", "0"],
        ["8", "8"],
        ["5", "5"],
        ["8", "2"],
    ]
    actual = get_coordinate_pairs()
    expected = (
        [
            [0, 9],
            [5, 9],
            [8, 0],
            [0, 8],
            [9, 4],
            [3, 4],
            [2, 2],
            [2, 1],
            [7, 0],
            [7, 4],
            [6, 4],
            [2, 0],
            [0, 9],
            [2, 9],
            [3, 4],
            [1, 4],
            [0, 0],
            [8, 8],
            [5, 5],
            [8, 2],
        ],
        9,
        9,
    )

    assert actual == expected, f"Returned {actual} instead of {expected}"
