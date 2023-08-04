from code_challenges.advent_of_code.chess_game import (
    find_pass_code,
    find_second_pass_code,
)


def test_find_pass_code_a():
    actual = find_pass_code("abc".encode("utf-8"))
    expected = "18f47a30"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_pass_code_b():
    actual = find_pass_code("wtnhxymk".encode("utf-8"))
    expected = "2414bc77"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_second_pass_code_a():
    actual = find_second_pass_code("abc".encode("utf-8"))
    expected = "05ace8e3"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_second_pass_code_b():
    actual = find_second_pass_code("wtnhxymk".encode("utf-8"))
    expected = "437e60fc"

    assert actual == expected, f"Returned {actual} instead of {expected}"
