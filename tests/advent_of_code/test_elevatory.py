from unittest.mock import patch


from code_challenges.advent_of_code.elevator import find_floor, enter_basement


@patch("code_challenges.advent_of_code.elevator.elevator_controls_input")
def test_find_floor(elevator_controls_input_mock):
    elevator_controls_input_mock.return_value = "(()()(((())"
    actual = find_floor()
    expected = 3

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.elevator.elevator_controls_input")
def test_enter_basement(elevator_controls_input_mock):
    elevator_controls_input_mock.return_value = "(()()))(((())"
    actual = enter_basement()
    expected = 7

    assert actual == expected, f"Returned {actual} instead of {expected}"
