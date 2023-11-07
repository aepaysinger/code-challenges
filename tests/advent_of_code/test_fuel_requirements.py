from unittest.mock import patch


from code_challenges.advent_of_code.fuel_requirements import (
    amount_of_fuel,
    fuel_for_fuel,
)


@patch("code_challenges.advent_of_code.fuel_requirements.get_modules")
def test_amount_of_fuel(get_modules_mock):
    get_modules_mock.return_value = [12, 14, 1969, 100756]
    actual = amount_of_fuel()
    expected = 34241

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.fuel_requirements.get_modules")
def test_fuel_for_fuel(get_modules_mock):
    get_modules_mock.return_value = [160, 1414, 1969, 100756]
    actual = fuel_for_fuel()
    expected = 52069

    assert actual == expected, f"Returned {actual} instead of {expected}"
