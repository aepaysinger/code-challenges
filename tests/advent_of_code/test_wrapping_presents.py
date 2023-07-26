from unittest.mock import patch


from code_challenges.advent_of_code.wrapping_presents import (
    find_dimensions,
    find_surface_area,
    ribbon_for_present,
)


@patch("code_challenges.advent_of_code.wrapping_presents.present_dimensions")
def test_find_dimensions(present_dimensions_mock):
    present_dimensions_mock.return_value = [
        "29x13x26",
        "11x11x14",
        "27x2x5",
        "6x10x13",
        "15x19x10",
    ]
    actual = find_dimensions()
    expected = [
        ["29", "13", "26"],
        ["11", "11", "14"],
        ["27", "2", "5"],
        ["6", "10", "13"],
        ["15", "19", "10"],
    ]

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.wrapping_presents.present_dimensions")
def test_find_surface_area(present_dimensions_mock):
    present_dimensions_mock.return_value = [
        "29x13x26",
        "11x11x14",
        "27x2x5",
        "6x10x13",
        "15x19x10",
    ]
    actual = find_surface_area()
    expected = 6659

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.wrapping_presents.present_dimensions")
def test_ribbon_for_present(present_dimensions_mock):
    present_dimensions_mock.return_value = [
        "29x13x26",
        "11x11x14",
        "27x2x5",
        "6x10x13",
        "15x19x10",
    ]
    actual = ribbon_for_present()
    expected = 15614

    assert actual == expected, f"Returned {actual} instead of {expected}"
