from code_challenges.code_wars.compare_substring_values import (
    find_substrings,
    find_highest_substring_value,
)


def test_find_substring():
    actual = find_substrings("strengthe")
    expected = [["s", "t", "r"], ["n", "g", "t", "h"]]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_highest_substring_value():
    actual = find_highest_substring_value([["s", "t", "r"], ["n", "g", "t", "h"]])
    expected = 57

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_substring_entire_alphabet():
    actual = find_substrings("qweraafstdxyhndbegvcfuilcoepsmznbuchdgywjkslwismhd")
    expected = [
        ["q", "w"],
        ["r"],
        ["f", "s", "t", "d", "x", "y", "h", "n", "d", "b"],
        ["g", "v", "c", "f"],
        ["l", "c"],
        ["p", "s", "m", "z", "n", "b"],
        ["c", "h", "d", "g", "y", "w", "j", "k", "s", "l", "w"],
        ["s", "m", "h", "d"],
    ]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_highest_substrinf_value_alphabet():
    actual = find_highest_substring_value(
        [
            ["q", "w"],
            ["r"],
            ["f", "s", "t", "d", "x", "y", "h", "n", "d", "b"],
            ["g", "v", "c", "f"],
            ["l", "c"],
            ["p", "s", "m", "z", "n", "b"],
            ["c", "h", "d", "g", "y", "w", "j", "k", "s", "l", "w"],
            ["s", "m", "h", "d"],
        ]
    )
    expected = 145

    assert actual == expected, f"Returned {actual} instead of {expected}"
