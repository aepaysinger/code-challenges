from unittest.mock import patch


from code_challenges.advent_of_code.tuning_trouble import (
    start_of_packet_marker,
    start_of_packet_message,
)


@patch("code_challenges.advent_of_code.tuning_trouble.get_code")
def test_start_of_packet_marker_a(tuning_trouble_mock):
    tuning_trouble_mock.return_value = "agyt"
    actual = start_of_packet_marker()
    expected = 4

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.tuning_trouble.get_code")
def test_start_of_packet_marker_b(tuning_trouble_mock):
    tuning_trouble_mock.return_value = "aggytttttftuyygy"
    actual = start_of_packet_marker()
    expected = 13

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.tuning_trouble.get_code")
def test_start_of_packet_message_a(tuning_trouble_mock):
    tuning_trouble_mock.return_value = "qwertyuiopasdf"
    actual = start_of_packet_message()
    expected = 14

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.tuning_trouble.get_code")
def test_start_of_packet_message_b(tuning_trouble_mock):
    tuning_trouble_mock.return_value = "qwertyuuiopabcdefghjkiasdf"
    actual = start_of_packet_message()
    expected = 21

    assert actual == expected, f"Returned {actual} instead of {expected}"
