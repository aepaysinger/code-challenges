from unittest.mock import patch

from code_challenges.advent_of_code.supply_stacks import (
    get_top_crates,
    get_top_crates_update,
)


@patch("code_challenges.advent_of_code.supply_stacks.get_moves")
def test_get_top_crates_a(get_moves_mock):
    get_moves_mock.return_value = [
        "move 1 from 8 to 1",
        "move 1 from 6 to 1",
        "move 3 from 7 to 4",
        "move 3 from 2 to 9",
        "move 11 from 9 to 3",
        "move 1 from 6 to 9",
        "move 15 from 3 to 9",
    ]
    actual = get_top_crates()
    expected = "SRHVZCMJW"

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.supply_stacks.get_moves")
def test_get_top_crates_b(get_moves_mock):
    get_moves_mock.return_value = [
        "move 1 from 8 to 1",
        "move 2 from 6 to 1",
        "move 3 from 7 to 4",
        "move 3 from 2 to 9",
        "move 4 from 4 to 3",
        "move 1 from 6 to 9",
        "move 3 from 3 to 9",
    ]
    actual = get_top_crates()
    expected = "LRVDZZMJD"

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.supply_stacks.get_moves")
def test_get_top_crates_update_a(get_moves_mock):
    get_moves_mock.return_value = [
        "move 1 from 8 to 1",
        "move 1 from 6 to 1",
        "move 3 from 7 to 4",
        "move 3 from 2 to 9",
        "move 11 from 9 to 3",
        "move 1 from 6 to 9",
        "move 15 from 3 to 9",
    ]
    actual = get_top_crates_update()
    expected = "SRHFZCMJJ"

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.supply_stacks.get_moves")
def test_get_top_crates_update_b(get_moves_mock):
    get_moves_mock.return_value = [
        "move 1 from 8 to 1",
        "move 2 from 6 to 1",
        "move 3 from 7 to 4",
        "move 3 from 2 to 9",
        "move 4 from 4 to 3",
        "move 1 from 6 to 9",
        "move 3 from 3 to 9",
    ]
    actual = get_top_crates_update()
    expected = "SRFDZZMJF"

    assert actual == expected, f"Returned {actual} instead of {expected}"
