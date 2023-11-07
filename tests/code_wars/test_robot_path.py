from code_challenges.code_wars.robot_path import RobotDirections, walk


def test_robot_directions_translate_directions():
    instructions = RobotDirections(">>")

    assert instructions.translate_directions() == "Take 2 steps right"


def test_robot_directions_walk_pause():
    actual = walk("")
    expected = "Paused"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_robot_directions_a():
    actual = walk("<<>")
    expected = "Take 2 steps left\nTake 1 step right"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_robot_directions_b():
    actual = walk("^^vvvv>><<^v>")
    expected = "Take 2 steps up\nTake 4 steps down\nTake 2 steps right\nTake 2 steps left\nTake 1 step up\nTake 1 step down\nTake 1 step right"

    assert actual == expected, f"Returned {actual} instead of {expected}"
