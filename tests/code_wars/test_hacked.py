from code_challenges.code_wars.hacked import find_hack


def test_find_hack_a():
    actual = find_hack(
        [
            ["Doe Lawrence", 200, ["B", "B", "B", "B", "A", "B"]],
            ["Jack Lawrence", 230, ["A", "A", "B", "B", "A", "B", "A", "A"]],
            ["Kabin Bradley", 200, ["B", "A", "A", "A", "A", "B", "A"]],
            ["Doe Webb", 80, ["B", "B", "A"]],
            ["Jack Black", 90, ["A", "A", "A"]],
        ]
    )
    expected = ["Doe Lawrence", "Jack Lawrence", "Kabin Bradley", "Doe Webb"]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_hack_b():
    actual = find_hack(
        [
            ["Violet Purple", 200, ["B", "F", "B", "B", "D", "B"]],
            ["Mint Green", 170, ["A", "A", "A", "A", "A"]],
            ["Sky Blue", 200, ["B", "A", "A", "A", "A", "B", "A"]],
            ["Brick Red", 80, ["B", "B", "A"]],
            ["Snow White", 90, ["A", "A", "A"]],
        ]
    )
    expected = ["Violet Purple", "Sky Blue", "Brick Red"]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_hack_c():
    actual = find_hack(
        [
            ["Midnight Blue", 200, ["B", "C", "B", "B", "D", "B"]],
            ["Dirt Brown", 170, ["A", "A", "A", "A", "A"]],
            ["Hot Pink", 145, ["C", "D", "B", "A", "A", "B", "A"]],
            ["Sun Yellow", 80, ["B", "B", "B"]],
            ["Sunset Orange", 110, ["A", "A", "A"]],
        ]
    )
    expected = ["Midnight Blue", "Sun Yellow", "Sunset Orange"]

    assert actual == expected, f"Returned {actual} instead of {expected}"
