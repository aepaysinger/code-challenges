from unittest.mock import patch

from code_challenges.advent_of_code.bathroom_security import find_code, find_code_2


@patch("code_challenges.advent_of_code.bathroom_security.get_key_pad_moves")
def test_find_code(mock_get_key_pad_moves):
    mock_get_key_pad_moves.return_value = ["ULL", "RRDDD", "LURDL", "UUUUD"]
    actual = find_code()
    expected = "1985"

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.bathroom_security.get_key_pad_moves")
def test_find_code_2(mock_get_key_pad_moves):
    mock_get_key_pad_moves.return_value = ["ULL", "RRDDD", "LURDL", "UUUUD"]
    actual = find_code_2()
    expected = "5DB3"

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.bathroom_security.get_key_pad_moves")
def test_find_code_2_2(mock_get_key_pad_moves):
    mock_get_key_pad_moves.return_value = ["RUDU", "RDRD", "LLDRU", "RRUDR", "LLRL"]
    actual = find_code_2()
    expected = "2C797"

    assert actual == expected, f"Returned {actual} instead of {expected}"
