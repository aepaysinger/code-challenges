from unittest.mock import patch


from code_challenges.advent_of_code.santas_route import follow_directions, robot_santa


@patch("code_challenges.advent_of_code.santas_route.get_directions")
def test_follow_directions(get_directions_mock):
    get_directions_mock.return_value = "<<v^>>"
    actual = follow_directions()
    expected = 4

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.santas_route.get_directions")
def test_robot_santa(get_directions_mock):
    get_directions_mock.return_value = "<<v^>>"
    actual = robot_santa()
    expected = 6

    assert actual == expected, f"Returned {actual} instead of {expected}"
