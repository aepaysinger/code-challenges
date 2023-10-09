from unittest.mock import patch


from code_challenges.advent_of_code.camp_cleanup import full_overlap, part_overlap


@patch("code_challenges.advent_of_code.camp_cleanup.camp_cleanup_sections")
def test_full_overlap_a(camp_cleanup_sections_mock):
    camp_cleanup_sections_mock.return_value = [
        "11-73,29-73",
        "43-82,44-44",
        "13-85,12-36",
        "69-80,5-44",
        "60-63,30-62",
        "21-21,21-79",
        "5-91,92-99",
        "1-5,4-9",
    ]
    actual = full_overlap()
    expected = 3

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.camp_cleanup.camp_cleanup_sections")
def test_full_overlap_b(camp_cleanup_sections_mock):
    camp_cleanup_sections_mock.return_value = [
        "3-90,65-89",
        "98-98,1-99",
        "40-43,19-42",
        "49-74,19-73",
        "33-84,3-84",
        "24-33,7-91",
    ]
    actual = full_overlap()
    expected = 4

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.camp_cleanup.camp_cleanup_sections")
def test_full_overlap_c(camp_cleanup_sections_mock):
    camp_cleanup_sections_mock.return_value = [
        "39-39,11-39",
        "17-94,17-95",
        "21-46,20-46",
        "2-99,3-98",
        "27-97,26-97",
        "3-43,34-83",
        "35-87,36-87",
        "30-90,31-89",
        "10-39,3-10",
        "61-92,15-62",
        "3-96,2-97",
        "59-85,86-92",
    ]
    actual = full_overlap()
    expected = 8

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.camp_cleanup.camp_cleanup_sections")
def test_part_overlap_a(camp_cleanup_sections_mock):
    camp_cleanup_sections_mock.return_value = [
        "11-73,29-73",
        "43-82,44-44",
        "13-85,12-36",
        "69-80,5-44",
        "60-63,30-62",
        "21-21,21-79",
        "5-91,92-99",
        "1-5,4-9",
    ]
    actual = part_overlap()
    expected = 6

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.camp_cleanup.camp_cleanup_sections")
def test_part_overlap_b(camp_cleanup_sections_mock):
    camp_cleanup_sections_mock.return_value = [
        "3-90,65-89",
        "98-98,1-99",
        "40-43,19-42",
        "49-74,19-73",
        "33-84,3-84",
        "24-33,7-91",
    ]
    actual = part_overlap()
    expected = 6

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.camp_cleanup.camp_cleanup_sections")
def test_part_overlap_c(camp_cleanup_sections_mock):
    camp_cleanup_sections_mock.return_value = [
        "39-39,11-39",
        "17-94,17-95",
        "21-46,20-46",
        "2-99,3-98",
        "27-97,26-97",
        "3-43,34-83",
        "35-87,36-87",
        "30-90,31-89",
        "10-39,3-10",
        "61-92,15-62",
        "3-96,2-97",
        "59-85,86-92",
    ]
    actual = part_overlap()
    expected = 11

    assert actual == expected, f"Returned {actual} instead of {expected}"
