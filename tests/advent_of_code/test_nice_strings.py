from unittest.mock import patch

from code_challenges.advent_of_code.nice_strings import (
    find_vowels,
    find_double_letter,
    find_subtext,
    find_double_pair,
    find_the_pattern,
    find_nice_string,
    find_nice_string_2,
)


def test_find_vowels_true():
    actual = find_vowels("aeiouaeiouaeiou")
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_vowels_false():
    actual = find_vowels("dvszwmarrgswjxmb")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_double_letter_true():
    actual = find_double_letter("ugknbfddgicrmopn")
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_double_letter_false():
    actual = find_double_letter("jchzalrnumimnmhp")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_subtext_true():
    actual = find_subtext("ugknbfddgicrmopn")
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_subtext_false():
    actual = find_subtext("haegwjzuvuyypxyu")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_double_pair_true():
    actual = find_double_pair("qjhvhtzxzqqjkmpb")
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_double_pair_false():
    actual = find_double_pair("ieodomkazucvgmuy")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_the_pattern_true():
    actual = find_the_pattern("qjhvhtzxzqqjkmpb")
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_the_pattern_false():
    actual = find_the_pattern("uurcxstgmygtbstg")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.nice_strings.get_text_to_check")
def test_find_nice_string(mock_get_text_to_check):
    mock_get_text_to_check.return_value = [
        "zpjxvrmaorjpwegy",
        "laxrlkntrukjcswz",
        "pbqoungonelthcke",
        "niexeyzvrtrlgfzw",
        "zuetendekblknqng",
        "lyazavyoweyuvfye",
        "tegbldtkagfwlerf",
        "xckozymymezzarpy",
        "ehydpjavmncegzfn",
        "jlnespnckgwmkkry",
        "bfyetscttekoodio",
    ]
    actual = find_nice_string()
    expected = 2

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.nice_strings.get_text_to_check")
def test_find_nice_string(mock_get_text_to_check):
    mock_get_text_to_check.return_value = [
        "qljhvhtzxxxzqqjkmpb",
        "xxyxx",
        "uurcxstgmygtbstg",
        "ieodomkazucvgmuy",
        "qjhvhtzxzqqjkmpb",
    ]
    actual = find_nice_string_2()
    expected = 2

    assert actual == expected, f"Returned {actual} instead of {expected}"
