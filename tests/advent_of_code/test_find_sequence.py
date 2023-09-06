from unittest.mock import patch

from code_challenges.advent_of_code.find_sequence import (
    find_aba,
    abba_in_middle,
    abba_on_outside,
)


@patch("code_challenges.advent_of_code.find_sequence.get_ip_addresses")
def test_abba_in_middle(mock_get_ip_addresses):
    mock_get_ip_addresses.return_value = [
        "abba[mnop]qrst",
        "abcd[bddb]xyyx",
        "aaaa[qwer]tyui",
        "ioxxoj[asdfgh]zxcvbn",
    ]
    actual = abba_in_middle()
    expected = ["abba[mnop]qrst", "aaaa[qwer]tyui", "ioxxoj[asdfgh]zxcvbn"]

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.find_sequence.get_ip_addresses")
def test_abba_on_outside(mock_get_ip_addresses):
    mock_get_ip_addresses.return_value = [
        "abba[mnop]qrst",
        "abcd[bddb]xyyx",
        "aaaa[qwer]tyui",
        "ioxxoj[asdfgh]zxcvbn",
    ]
    actual = abba_on_outside()
    expected = 2

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.find_sequence.get_ip_addresses")
def test_find_aba(mock_get_ip_addresses):
    mock_get_ip_addresses.return_value = [
        "aba[bab]xyz",
        "xyx[xyx]xyx",
        "aaa[kek]eke",
        "zazbz[bzb]cdb",
    ]
    actual = find_aba()
    expected = 3

    assert actual == expected, f"Returned {actual} instead of {expected}"
