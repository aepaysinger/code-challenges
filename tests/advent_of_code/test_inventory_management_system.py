from unittest.mock import patch


from code_challenges.advent_of_code.inventory_management_system import (
    get_id_counts,
    find_box_ids_checksum,
    compare_boxes,
    find_similar_box,
)


@patch("code_challenges.advent_of_code.inventory_management_system.get_box_ids")
def test_get_id_counts(mock_get_box_ids):
    mock_get_box_ids.return_value = [
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
        "fguij",
        "axcye",
        "wvxyz",
    ]
    actual = get_id_counts()
    expected = {
        "abcde": {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1},
        "fghij": {"f": 1, "g": 1, "h": 1, "i": 1, "j": 1},
        "klmno": {"k": 1, "l": 1, "m": 1, "n": 1, "o": 1},
        "pqrst": {"p": 1, "q": 1, "r": 1, "s": 1, "t": 1},
        "fguij": {"f": 1, "g": 1, "u": 1, "i": 1, "j": 1},
        "axcye": {"a": 1, "x": 1, "c": 1, "y": 1, "e": 1},
        "wvxyz": {"w": 1, "v": 1, "x": 1, "y": 1, "z": 1},
    }

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.inventory_management_system.get_box_ids")
def test_find_box_ids_checksum(mock_get_box_ids):
    mock_get_box_ids.return_value = [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab",
    ]
    actual = find_box_ids_checksum()
    expected = 12

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_compare_boxes_a():
    actual = compare_boxes(
        {"f": 1, "g": 1, "h": 1, "i": 1, "j": 1},
        {"f": 1, "g": 1, "u": 1, "i": 1, "j": 1},
    )
    expected = (True, ["h", "u"])

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_compare_boxes_b():
    actual = compare_boxes(
        {"a": 2, "b": 1, "c": 1, "d": 1, "e": 1},
        {"a": 1, "x": 1, "c": 2, "y": 1, "e": 1},
    )
    expected = (False, ["a", "b", "c", "d", "a", "x", "c", "y"])

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.inventory_management_system.get_box_ids")
def test_find_similar_box(mock_get_box_ids):
    mock_get_box_ids.return_value = [
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
        "fguij",
        "axcye",
        "wvxyz",
    ]
    actual = find_similar_box()
    expected = "fgij"

    assert actual == expected, f"Returned {actual} instead of {expected}"
