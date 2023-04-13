from unittest.mock import patch


from code_challenges.advent_of_code.crossed_wires import (
    find_closest_to_starting_point,
    find_where_wires_cross,
    find_wires_path,
)


@patch("code_challenges.advent_of_code.crossed_wires.get_wires_path")
def test_find_wires_path(get_wires_path_mock):
    get_wires_path_mock.return_value = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
    actual = find_wires_path()
    expected = (
        {8: [(0, 5)], 3: [(5, 2)]},
        {0: [(0, 8)], 5: [(8, 3)]},
        {0: [(0, 7)], 6: [(7, 3)]},
        {7: [(0, 6)], 3: [(6, 2)]},
    )

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.crossed_wires.get_wires_path")
def test_find_where_wires_cross(get_wires_path_mock):
    get_wires_path_mock.return_value = [
        "R75,D30,R83,U83,L12,D49,R71,U7,L72",
        "U62,R66,U55,R34,D71,R55,D58,R83",
    ]
    actual = find_where_wires_cross()
    expected = [(146, 46), (158, -12), (155, 4), (155, 11)]

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.crossed_wires.get_wires_path")
def test_find_closest_to_starting_point(get_wires_path_mock):
    get_wires_path_mock.return_value = [
        "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
        "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
    ]
    actual = find_closest_to_starting_point()
    expected = 135

    assert actual == expected, f"Returned {actual} instead of {expected}"
