from code_challenges.code_wars.unscrambled_eggs import unscrambled_eggs


def test_unscrambled_eggs_a():
    actual = unscrambled_eggs("ceggodegge heggeregge")
    expected = "code here"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_unscrambled_eggs_b():
    actual = unscrambled_eggs("FeggUNegg KeggATeggA")
    expected = "FUN KATA"

    assert actual == expected, f"Returned {actual} instead of {expected}"
