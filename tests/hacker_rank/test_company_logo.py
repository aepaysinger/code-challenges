from code_challenges.hacker_rank.company_logo import make_logo


def test_make_logo_in_order():
    actual = make_logo("aaaaabbbbcccdde")
    expected = "a 5\nb 4\nc 3"

    assert actual == expected, f"Returned {actual} but should have returned {expected}"


def test_make_logo_out_of_order():
    actual = make_logo("hhhrrvvvaaaaaauupppllesqqbbbzzzzzzzzzz")
    expected = "z 10\na 6\nb 3"

    assert actual == expected, f"Returned {actual} but should have returned {expected}"


def test_make_logo_tie_out_of_order():
    actual = make_logo("pygzaimbetc")
    expected = "a 1\nb 1\nc 1"

    assert actual == expected, f"Returned {actual} but should have returned {expected}"


def test_make_logo_with_space():
    actual = make_logo("aa bb cc dd")
    expected = "a 2\nb 2\nc 2"

    assert actual == expected, f"Returned {actual} but should have returned {expected}"
