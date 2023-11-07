from unittest.mock import patch

from code_challenges.advent_of_code.binary_diagnostic import (
    find_submarine_power_consumption,
    life_support_rating,
)


@patch("code_challenges.advent_of_code.binary_diagnostic.get_diagnostic_report")
def test_find_submarine_power_consumption(mock_get_diagnostic_report):
    mock_get_diagnostic_report.return_value = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    actual = find_submarine_power_consumption()
    expected = 198

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.binary_diagnostic.get_diagnostic_report")
def test_find_life_support_rating(mock_get_diagnostic_report):
    mock_get_diagnostic_report.return_value = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    actual = life_support_rating()
    expected = 230

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.binary_diagnostic.get_diagnostic_report")
def test_find_submarine_power_consumption_a(mock_get_diagnostic_report):
    mock_get_diagnostic_report.return_value = [
        "00100",
        "01110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "00000",
        "11001",
        "00010",
        "01010",
    ]
    actual = find_submarine_power_consumption()
    expected = 150

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.binary_diagnostic.get_diagnostic_report")
def test_find_life_support_rating_a(mock_get_diagnostic_report):
    mock_get_diagnostic_report.return_value = [
        "00100",
        "01110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "00000",
        "11001",
        "00010",
        "01010",
    ]
    actual = life_support_rating()
    expected = 175

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.binary_diagnostic.get_diagnostic_report")
def test_find_life_support_rating_b(mock_get_diagnostic_report):
    mock_get_diagnostic_report.return_value = [
        "01100",
        "01110",
        "00110",
        "10111",
        "10001",
        "01111",
        "00111",
        "11100",
        "00000",
        "11001",
        "00010",
        "01010",
    ]
    actual = life_support_rating()
    expected = 255

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.binary_diagnostic.get_diagnostic_report")
def test_find_life_support_rating_c(mock_get_diagnostic_report):
    mock_get_diagnostic_report.return_value = [
        "11100",
        "11110",
        "10110",
        "10111",
        "10001",
        "11111",
        "00111",
        "11100",
        "00000",
        "11001",
        "00010",
        "01010",
    ]
    actual = life_support_rating()
    expected = 310

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.binary_diagnostic.get_diagnostic_report")
def test_find_life_support_rating_d(mock_get_diagnostic_report):
    mock_get_diagnostic_report.return_value = [
        "00100",
        "00100",
        "10110",
        "11111",
        "10001",
        "01111",
        "00111",
        "11100",
        "11000",
        "11001",
        "00010",
        "01010",
    ]
    actual = life_support_rating()
    expected = 476

    assert actual == expected, f"Returned {actual} instead of {expected}"
