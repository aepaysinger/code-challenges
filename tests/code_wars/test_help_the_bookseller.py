from code_challenges.code_wars.help_the_bookseller import help_the_bookseller


def test_help_the_bookseller():
    actual = help_the_bookseller(
        ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 10", "DRTY 600"],
        ["B", "A", "D", "E"],
    )
    expected = "(B : 410) - (A : 0) - (D : 600) - (E : 0)"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_help_the_bookseller_all_0():
    actual = help_the_bookseller(
        ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 10", "DRTY 600"],
        ["Z", "A", "K", "E"],
    )
    expected = ""

    assert actual == expected, f"Returned {actual} instead of {expected}"
