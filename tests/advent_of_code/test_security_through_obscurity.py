from unittest.mock import patch

from code_challenges.advent_of_code.security_through_obscurity import (
    by_number,
    by_letter,
    get_encrypted_room_name,
    translate_room_names,
    get_room_names,
)


@patch("code_challenges.advent_of_code.security_through_obscurity.get_room_names")
def test_by_number(mock_room_name_input):
    mock_room_name_input.return_value = [
        "aaaaa-bbb-z-y-x-123[abxyz]",
        "a-b-c-d-e-f-g-h-987[abcde]",
        "not-a-real-room-404[oarel]",
        "totally-real-room-200[decoy]",
    ]
    actual = by_number(("a", 5))
    expected = 5

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.security_through_obscurity.get_room_names")
def test_by_letter(mock_room_name_input):
    mock_room_name_input.return_value = [
        "aaaaa-bbb-z-y-x-123[abxyz]",
        "a-b-c-d-e-f-g-h-987[abcde]",
        "not-a-real-room-404[oarel]",
        "totally-real-room-200[decoy]",
    ]
    actual = by_letter(("a", 5))
    expected = "a"

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.security_through_obscurity.get_room_names")
def test_get_encrypted_room_name(mock_room_name_input):
    mock_room_name_input.return_value = [
        "aaaaa-bbb-z-y-x-123[abxyz]",
        "a-b-c-d-e-f-g-h-987[abcde]",
        "not-a-real-room-404[oarel]",
        "totally-real-room-200[decoy]",
    ]
    actual = get_encrypted_room_name()
    expected = (
        1514,
        [
            ["aaaaa", "bbb", "z", "y", "x", "123[abxyz]"],
            ["a", "b", "c", "d", "e", "f", "g", "h", "987[abcde]"],
            ["not", "a", "real", "room", "404[oarel]"],
        ],
    )

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.security_through_obscurity.get_room_names")
def test_translate_room_names(mock_room_name_input):
    mock_room_name_input.return_value = [
        "aczupnetwp-mfyyj-opalcexpye-977[peyac]",
        "qzchnzbshud-cxd-trdq-sdrshmf-105[jqexn]",
        "molgbzqfib-bdd-mrozexpfkd-289[bdfmo]",
        "enzcntvat-pnaql-qrfvta-351[antqv]",
        "otzkxtgzoutgr-jek-vaxingyotm-670[tgokx]",
    ]
    actual = translate_room_names("projectile egg purchasing ")
    expected = 289

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.security_through_obscurity.get_room_names")
def test_translate_room_names_a(mock_room_name_input):
    mock_room_name_input.return_value = [
        "aczupnetwp-mfyyj-opalcexpye-977[peyac]",
        "qzchnzbshud-cxd-trdq-sdrshmf-105[jqexn]",
        "molgbzqfib-bdd-mrozexpfkd-289[bdfmo]",
        "enzcntvat-pnaql-qrfvta-351[antqv]",
        "otzkxtgzoutgr-jek-vaxingyotm-670[tgokx]",
    ]
    actual = translate_room_names("north pole ")
    expected = [
        "projectile bunny department",
        "projectile egg purchasing",
        "rampaging candy design",
        "international dye purchasing",
    ]

    assert actual == expected, f"Returned {actual} instead of {expected}"


class MockFile:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def read(self):
        return "aczupnetwp-mfyyj-opalcexpye-977[peyac]\nqzchnzbshud-cxd-trdq-sdrshmf-105[jqexn]\nmolgbzqfib-bdd-mrozexpfkd-289[bdfmo]"


@patch("code_challenges.advent_of_code.security_through_obscurity.open")
def test_get_room_names(mock_open):
    mock_open.return_value = MockFile()
    actual = get_room_names()
    expected = [
        "aczupnetwp-mfyyj-opalcexpye-977[peyac]",
        "qzchnzbshud-cxd-trdq-sdrshmf-105[jqexn]",
        "molgbzqfib-bdd-mrozexpfkd-289[bdfmo]",
    ]

    assert actual == expected, f"Returned {actual} instead of {expected}"
