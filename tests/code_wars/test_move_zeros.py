from code_challenges.code_wars.move_zeros import move_zeros


def test_move_zeros():
    actual = move_zeros([1, 0, 1, 2, 0, 1, 3])
    expected = [1, 1, 2, 1, 3, 0, 0]

    assert actual == expected, f"Should have returned {expected} but returned {actual}"


def test_move_zeros_no_zeros():
    actual = move_zeros([3, 5, 2, 9, 4, 8])
    expected = [3, 5, 2, 9, 4, 8]

    assert actual == expected, f"Should have returned {expected} but returned {actual}"


def test_move_zeros_empty_list():
    actual = move_zeros([])
    expected = []

    assert actual == expected, f"Should have returned {expected} but returned {actual}"


def test_move_zeros_all_zeros():
    actual = move_zeros([0, 0, 0, 0])
    expected = [0, 0, 0, 0]

    assert actual == expected, f"Should have returned {expected} but returned {actual}"
