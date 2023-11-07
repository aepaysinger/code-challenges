from code_challenges.code_wars.popping_blocks import pop_blocks


def test_popping_blacks_a():
    actual = pop_blocks(["A", "B", "C", "C", "B", "D", "A"])
    expected = ["A", "D", "A"]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_popping_blacks_b():
    actual = pop_blocks(["A", "B", "A", "A", "A", "B", "B"])
    expected = ["A"]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_popping_blacks_c():
    actual = pop_blocks(["B", "B", "C", "C", "A", "A", "A"])
    expected = []

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_popping_blacks_d():
    actual = pop_blocks(["A", "B", "C", "A", "B", "C"])
    expected = ["A", "B", "C", "A", "B", "C"]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_popping_blacks_e():
    actual = pop_blocks([])
    expected = []

    assert actual == expected, f"Returned {actual} instead of {expected}"
