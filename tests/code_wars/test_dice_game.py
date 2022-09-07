from code_challenges.code_wars.dice_game import dice_game


def test_dice_game_one_number():
    actual = dice_game([5, 5, 5, 5, 5])
    expected = 600

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_dice_game_no_points():
    actual = dice_game([2, 3, 4, 6, 2])
    expected = 0

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_dice_game_mixed_points():
    actual = dice_game([1, 5, 1, 1, 4])
    expected = 1050

    assert actual == expected, f"Returned {actual} instead of {expected}"
