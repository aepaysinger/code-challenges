from unittest.mock import patch

from code_challenges.advent_of_code.repetition_code import (
    break_up_messages,
    find_hidden_message_high,
    find_hidden_message_low,
)


@patch("code_challenges.advent_of_code.repetition_code.get_messages")
def test_break_up_messages(mock_get_messages):
    mock_get_messages.return_value = [
        "eedadn",
        "drvtee",
        "eandsr",
        "raavrd",
        "atevrs",
        "tsrnev",
        "sdttsa",
        "rasrtv",
        "nssdts",
        "ntnada",
        "svetve",
        "tesnvt",
        "vntsnd",
        "vrdear",
        "dvrsen",
        "enarar",
    ]
    actual = break_up_messages()
    expected = {
        "position 0": {"e": 3, "d": 2, "r": 2, "a": 1, "t": 2, "s": 2, "n": 2, "v": 2},
        "position 1": {"e": 2, "r": 2, "a": 3, "t": 2, "s": 2, "d": 1, "v": 2, "n": 2},
        "position 2": {"d": 2, "v": 1, "n": 2, "a": 2, "e": 2, "r": 2, "t": 2, "s": 3},
        "position 3": {"a": 2, "t": 3, "d": 2, "v": 2, "n": 2, "r": 2, "s": 2, "e": 1},
        "position 4": {"d": 2, "e": 3, "s": 2, "r": 2, "t": 2, "v": 2, "n": 1, "a": 2},
        "position 5": {"n": 2, "e": 2, "r": 3, "d": 2, "s": 2, "v": 2, "a": 2, "t": 1},
    }

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.repetition_code.get_messages")
def test_find_hidden_message_high(mock_get_messages):
    mock_get_messages.return_value = [
        "eedadn",
        "drvtee",
        "eandsr",
        "raavrd",
        "atevrs",
        "tsrnev",
        "sdttsa",
        "rasrtv",
        "nssdts",
        "ntnada",
        "svetve",
        "tesnvt",
        "vntsnd",
        "vrdear",
        "dvrsen",
        "enarar",
    ]
    actual = find_hidden_message_high()
    expected = "easter"

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.repetition_code.get_messages")
def test_find_hidden_message_low(mock_get_messages):
    mock_get_messages.return_value = [
        "eedadn",
        "drvtee",
        "eandsr",
        "raavrd",
        "atevrs",
        "tsrnev",
        "sdttsa",
        "rasrtv",
        "nssdts",
        "ntnada",
        "svetve",
        "tesnvt",
        "vntsnd",
        "vrdear",
        "dvrsen",
        "enarar",
    ]
    actual = find_hidden_message_low()
    expected = "advent"

    assert actual == expected, f"Returned {actual} instead of {expected}"
