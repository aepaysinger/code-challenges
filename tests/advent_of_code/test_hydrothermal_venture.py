from unittest.mock import patch

from code_challenges.advent_of_code.hydrothermal_venture import transform_vents_input, get_coordinate_pairs, count_coordinate_points


@patch("code_challenges.advent_of_code.hydrothermal_venture.get_vents_input")
def test_transform_vents_input(mock_get_vents_input):
    mock_get_vents_input.return_value = ['0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1', '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9', '3,4 -> 1,4', '0,0 -> 8,8', '5,5 -> 8,2']
    actual = transform_vents_input()
    expected = [['0', '9'], ['5', '9'], ['8', '0'], ['0', '8'], ['9', '4'], ['3', '4'], ['2', '2'], ['2', '1'], ['7', '0'], ['7', '4'], ['6', '4'], ['2', '0'], ['0', '9'], ['2', '9'], ['3', '4'], ['1', '4'], ['0', '0'], ['8', '8'], ['5', '5'], ['8', '2']]

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.hydrothermal_venture.get_vents_input")
def test_get_coordinate_pairs(mock_get_vents_input):
    mock_get_vents_input.return_value = ['0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1', '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9', '3,4 -> 1,4', '0,0 -> 8,8', '5,5 -> 8,2']
    actual = get_coordinate_pairs()
    expected = [[(0, 9), (5, 9)], [(8, 0), (0, 8)], [(9, 4), (3, 4)], [(2, 2), (2, 1)], [(7, 0), (7, 4)], [(6, 4), (2, 0)], [(0, 9), (2, 9)], [(3, 4), (1, 4)], [(0, 0), (8, 8)], [(5, 5), (8, 2)]]

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.hydrothermal_venture.get_vents_input")
def test_count_coordinate_points(mock_get_vents_input):
    mock_get_vents_input.return_value = ['0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1', '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9', '3,4 -> 1,4', '0,0 -> 8,8', '5,5 -> 8,2']
    actual = count_coordinate_points()
    expected = 12

    assert actual == expected, f"Returned {actual} instead of {expected}"

