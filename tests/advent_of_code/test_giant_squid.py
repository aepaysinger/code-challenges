from unittest.mock import patch

from code_challenges.advent_of_code.giant_squid import (
    play_bingo,
    find_winner_score,
    find_last_winning_board,
    find_last_winner_score,
)


@patch("code_challenges.advent_of_code.giant_squid.get_bingo_info")
def test_play_bingo(mock_get_bingo_info):
    mock_get_bingo_info.return_value = (
        {
            1: [
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19],
            ],
            2: [
                [3, 15, 0, 2, 22],
                [9, 18, 13, 17, 5],
                [19, 8, 7, 25, 23],
                [20, 11, 10, 24, 4],
                [14, 21, 16, 12, 6],
            ],
            3: [
                [14, 21, 17, 24, 4],
                [10, 16, 15, 9, 19],
                [18, 8, 23, 26, 20],
                [22, 11, 13, 6, 5],
                [2, 0, 12, 3, 7],
            ],
        },
        [
            7,
            4,
            9,
            5,
            11,
            17,
            23,
            2,
            0,
            14,
            21,
            24,
            10,
            16,
            13,
            6,
            15,
            25,
            12,
            22,
            18,
            20,
            8,
            19,
            3,
            26,
            1,
        ],
    )

    actual = play_bingo()
    expected = (
        [
            ["X", "X", "X", "X", "X"],
            [10, 16, 15, "X", 19],
            [18, 8, "X", 26, 20],
            [22, "X", 13, 6, "X"],
            ["X", "X", 12, 3, "X"],
        ],
        24,
    )

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.giant_squid.get_bingo_info")
def test_play_bingo_a(mock_get_bingo_info):
    mock_get_bingo_info.return_value = (
        {
            1: [
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19],
            ],
            2: [
                [3, 15, 0, 2, 22],
                [9, 18, 13, 17, 5],
                [19, 8, 7, 25, 23],
                [20, 11, 10, 24, 4],
                [14, 21, 16, 12, 6],
            ],
            3: [
                [14, 21, 17, 24, 4],
                [10, 16, 15, 9, 19],
                [18, 8, 23, 26, 20],
                [22, 11, 13, 6, 5],
                [2, 0, 12, 3, 7],
            ],
        },
        [
            22,
            8,
            21,
            6,
            1,
            7,
            4,
            9,
            5,
            11,
            17,
            23,
            2,
            0,
            14,
            21,
            24,
            10,
            16,
            13,
            6,
            15,
            25,
            12,
            22,
            18,
            20,
            8,
            19,
            3,
            26,
            1,
        ],
    )

    actual = play_bingo()
    expected = (
        [
            ["X", 13, 17, 11, 0],
            ["X", 2, 23, 4, 24],
            ["X", 9, 14, 16, 7],
            ["X", 10, 3, 18, 5],
            ["X", 12, 20, 15, 19],
        ],
        1,
    )

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.giant_squid.get_bingo_info")
def test_find_winner_score(mock_get_bingo_info):
    mock_get_bingo_info.return_value = (
        {
            1: [
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19],
            ],
            2: [
                [3, 15, 0, 2, 22],
                [9, 18, 13, 17, 5],
                [19, 8, 7, 25, 23],
                [20, 11, 10, 24, 4],
                [14, 21, 16, 12, 6],
            ],
            3: [
                [14, 21, 17, 24, 4],
                [10, 16, 15, 9, 19],
                [18, 8, 23, 26, 20],
                [22, 11, 13, 6, 5],
                [2, 0, 12, 3, 7],
            ],
        },
        [
            7,
            4,
            9,
            5,
            11,
            17,
            23,
            2,
            0,
            14,
            21,
            24,
            10,
            16,
            13,
            6,
            15,
            25,
            12,
            22,
            18,
            20,
            8,
            19,
            3,
            26,
            1,
        ],
    )

    actual = find_winner_score()
    expected = 4512

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.giant_squid.get_bingo_info")
def test_find_last_winning_board(mock_get_bingo_info):
    mock_get_bingo_info.return_value = (
        {
            1: [
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19],
            ],
            2: [
                [3, 15, 0, 2, 22],
                [9, 18, 13, 17, 5],
                [19, 8, 7, 25, 23],
                [20, 11, 10, 24, 4],
                [14, 21, 16, 12, 6],
            ],
            3: [
                [14, 21, 17, 24, 4],
                [10, 16, 15, 9, 19],
                [18, 8, 23, 26, 20],
                [22, 11, 13, 6, 5],
                [2, 0, 12, 3, 7],
            ],
        },
        [
            7,
            4,
            9,
            5,
            11,
            17,
            23,
            2,
            0,
            14,
            21,
            24,
            10,
            16,
            13,
            6,
            15,
            25,
            12,
            22,
            18,
            20,
            8,
            19,
            3,
            26,
            1,
        ],
    )

    actual = find_last_winning_board()
    expected = (
        [
            [3, 15, "X", "X", 22],
            ["X", 18, "X", "X", "X"],
            [19, 8, "X", 25, "X"],
            [20, "X", "X", "X", "X"],
            ["X", "X", "X", 12, 6],
        ],
        13,
    )

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.giant_squid.get_bingo_info")
def test_find_last_winning_board_a(mock_get_bingo_info):
    mock_get_bingo_info.return_value = (
        {
            1: [
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19],
            ],
            2: [
                [3, 15, 0, 2, 22],
                [9, 18, 13, 17, 5],
                [19, 8, 7, 25, 23],
                [20, 11, 10, 24, 4],
                [14, 21, 16, 12, 6],
            ],
            3: [
                [14, 21, 17, 24, 4],
                [10, 16, 15, 9, 19],
                [18, 8, 23, 26, 20],
                [22, 11, 13, 6, 5],
                [2, 0, 12, 3, 7],
            ],
        },
        [22, 8, 21, 6, 1, 5, 23, 4, 6, 18, 26, 20],
    )

    actual = find_last_winning_board()
    expected = (
        [
            [14, "X", 17, 24, "X"],
            [10, 16, 15, 9, 19],
            ["X", "X", "X", "X", "X"],
            ["X", 11, 13, "X", "X"],
            [2, 0, 12, 3, 7],
        ],
        20,
    )

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.giant_squid.get_bingo_info")
def test_find_last_winner_score(mock_get_bingo_info):
    mock_get_bingo_info.return_value = (
        {
            1: [
                [22, 13, 17, 11, 0],
                [8, 2, 23, 4, 24],
                [21, 9, 14, 16, 7],
                [6, 10, 3, 18, 5],
                [1, 12, 20, 15, 19],
            ],
            2: [
                [3, 15, 0, 2, 22],
                [9, 18, 13, 17, 5],
                [19, 8, 7, 25, 23],
                [20, 11, 10, 24, 4],
                [14, 21, 16, 12, 6],
            ],
            3: [
                [14, 21, 17, 24, 4],
                [10, 16, 15, 9, 19],
                [18, 8, 23, 26, 20],
                [22, 11, 13, 6, 5],
                [2, 0, 12, 3, 7],
            ],
        },
        [
            7,
            4,
            9,
            5,
            11,
            17,
            23,
            2,
            0,
            14,
            21,
            24,
            10,
            16,
            13,
            6,
            15,
            25,
            12,
            22,
            18,
            20,
            8,
            19,
            3,
            26,
            1,
        ],
    )

    actual = find_last_winner_score()
    expected = 1924

    assert actual == expected, f"Returned {actual} instead of {expected}"
