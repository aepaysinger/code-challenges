from code_challenges.code_wars.cut_rope import cut_rope


def test_cut_rope_a():
    actual = cut_rope(6, 2, 3)
    expected = {"1cm": 2, "2cm": 2}

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_cut_rope_b():
    actual = cut_rope(11, 2, 5)
    expected = {"1cm": 3, "2cm": 4}

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_cut_rope_c():
    actual = cut_rope(7, 2, 3)
    expected = {"1cm": 3, "2cm": 2}

    assert actual == expected, f"Returned {actual} instead of {expected}"
