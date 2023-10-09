from code_challenges.code_wars.directions_reduction import (
    directions_reduction_a,
    directions_reduction_b,
)


def test_directions_reduction_a():
    actual = directions_reduction_a(
        ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    )
    expected = ["WEST"]

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_directions_reduction_b():
    actual = directions_reduction_a(["NORTH", "WEST", "SOUTH", "EAST"])
    expected = ["NORTH", "WEST", "SOUTH", "EAST"]

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_directions_reduction_c():
    actual = directions_reduction_b(
        ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    )
    expected = ["WEST"]

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_directions_reduction_d():
    actual = directions_reduction_b(["NORTH", "WEST", "SOUTH", "EAST"])
    expected = ["NORTH", "WEST", "SOUTH", "EAST"]

    assert actual == expected, f"Returned {actual} instead of {expected}."
