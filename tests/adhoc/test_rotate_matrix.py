from code_challenges.adhoc.rotate_matrix import rotate_matrix, rotate_v2, rotate_v3


def test_rotate_matrix_4_x_4():
    actual = rotate_matrix(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
    )
    expected = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_rotate_matrix_3_x_3():
    actual = rotate_matrix(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    )
    expected = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_rotate_v2_4_x_4():
    actual = rotate_matrix(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
    )
    expected = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_rotate_v2_3_x_3():
    actual = rotate_matrix(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    )
    expected = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_rotate_v3_4_x_4():
    actual = rotate_matrix(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
    )
    expected = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_rotate_v3_3_x_3():
    actual = rotate_matrix(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    )
    expected = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    assert actual == expected, f"Returned {actual} instead of {expected}"
