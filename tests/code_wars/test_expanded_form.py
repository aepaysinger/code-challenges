from code_challenges.code_wars.expanded_form import expanded_form


def test_expanded_form_A():
    actual = expanded_form(12)
    expected = "10 + 2"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_expanded_form_B():
    actual = expanded_form(437)
    expected = "400 + 30 + 7"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_expanded_form_C():
    actual = expanded_form(800602)
    expected = "800000 + 600 + 2"

    assert actual == expected, f"Returned {actual} instead of {expected}"
