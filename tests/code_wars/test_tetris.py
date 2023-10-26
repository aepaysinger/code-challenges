from code_challenges.code_wars.tetris import tetris


def test_tetris_a():
    actual = tetris(["4R4", "4L3", "4L2", "4L1", "4L0", "4R1", "4R2", "4R3", "3L4"])
    expected = 3

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_tetris_b():
    actual = tetris(
        [
            "2L2",
            "2L1",
            "4L1",
            "4R4",
            "3L2",
            "3R0",
            "4R1",
            "4R0",
            "1L4",
            "2L1",
            "3L4",
            "3L2",
            "2R3",
            "3R0",
            "4R4",
            "3R2",
            "1R2",
            "3L3",
            "4R3",
            "4R1",
            "2L2",
            "3R0",
            "1L2",
            "3R0",
            "1L1",
            "1L4",
            "3R1",
            "2L1",
            "1L3",
            "3R2",
        ]
    )
    expected = 4

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_tetris_c():
    actual = tetris(["1L2", "4R2", "3L3", "3L1", "1L4", "1R4"])
    expected = 0

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_tetris_d():
    actual = tetris(
        [
            "4L4",
            "1L3",
            "1L2",
            "1L1",
            "1L0",
            "1R1",
            "1R2",
            "1R3",
            "1R4",
            "4L4",
            "4L4",
            "4L4",
            "4L4",
            "4L4",
            "4L4",
            "4L4",
            "1L3",
            "1L2",
            "1L1",
            "1L0",
            "1R1",
            "1R2",
            "1R3",
            "1R4",
        ]
    )
    expected = 1

    assert actual == expected, f"Returned {actual} instead of {expected}"
