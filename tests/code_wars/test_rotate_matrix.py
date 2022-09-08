from code_challenges.code_wars.rotate_matrix import rotate_matrix


def test_rotate_matrix_4_x_4():
    actual = rotate_matrix([
        [1,2,3,8],
        [4,5,6,8],
        [7,8,9,8],
        [9,8,7,6],
    ])
    expected = [
        [9, 7, 4, 1],
        [8, 8, 5, 2],
        [7, 9, 6, 3],
        [6, 8, 8, 8],
    ]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_rotate_matrix_3_x_3():
    actual = rotate_matrix([
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ])
    expected = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    assert actual == expected, f"Returned {actual} instead of {expected}"