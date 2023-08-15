from unittest.mock import patch

from code_challenges.advent_of_code.fabric_prototype import (
    break_down_claims_info,
    find_overlap,
    find_no_overlap,
    organize_claim_info,
)


@patch("code_challenges.advent_of_code.fabric_prototype.get_elf_claims")
def test_break_down_claims_info(mock_get_elf_claims):
    mock_get_elf_claims.return_value = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2",
    ]
    actual = break_down_claims_info()
    expected = [
        ["#1", "@", "1,3:", "4x4"],
        ["#2", "@", "3,1:", "4x4"],
        ["#3", "@", "5,5:", "2x2"],
    ]

    assert actual == expected, f"Returned {actual} instrad of {expected}"


@patch("code_challenges.advent_of_code.fabric_prototype.get_elf_claims")
def test_find_overlap(mock_get_elf_claims):
    mock_get_elf_claims.return_value = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2",
    ]
    actual = find_overlap()
    expected = (
        4,
        {
            (1, 3): 1,
            (1, 4): 1,
            (1, 5): 1,
            (1, 6): 1,
            (2, 3): 1,
            (2, 4): 1,
            (2, 5): 1,
            (2, 6): 1,
            (3, 3): 2,
            (3, 4): 2,
            (3, 5): 1,
            (3, 6): 1,
            (4, 3): 2,
            (4, 4): 2,
            (4, 5): 1,
            (4, 6): 1,
            (3, 1): 1,
            (3, 2): 1,
            (4, 1): 1,
            (4, 2): 1,
            (5, 1): 1,
            (5, 2): 1,
            (5, 3): 1,
            (5, 4): 1,
            (6, 1): 1,
            (6, 2): 1,
            (6, 3): 1,
            (6, 4): 1,
            (5, 5): 1,
            (5, 6): 1,
            (6, 5): 1,
            (6, 6): 1,
        },
    )

    assert actual == expected, f"Returned {actual} instrad of {expected}"


@patch("code_challenges.advent_of_code.fabric_prototype.get_elf_claims")
def test_find_no_overlap(mock_get_elf_claims):
    mock_get_elf_claims.return_value = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2",
    ]
    actual = find_no_overlap()
    expected = "#3"

    assert actual == expected, f"Returned {actual} instrad of {expected}"


@patch("code_challenges.advent_of_code.fabric_prototype.get_elf_claims")
def test_organize_claim_info(mock_get_elf_claims):
    mock_get_elf_claims.return_value = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2",
    ]
    actual = organize_claim_info()
    expected = {
        "#1": [(1, 3), ("4", "4")],
        "#2": [(3, 1), ("4", "4")],
        "#3": [(5, 5), ("2", "2")],
    }

    assert actual == expected, f"Returned {actual} instrad of {expected}"
