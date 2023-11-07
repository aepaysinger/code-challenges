from code_challenges.code_wars.pig_latin import pig_it


def test_pig_it_a():
    actual = pig_it("Pig latin is cool")
    expected = "igPay atinlay siay oolcay"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_pig_it_b():
    actual = pig_it("Hello world !")
    expected = "elloHay orldway !"

    assert actual == expected, f"Returned {actual} instead of {expected}"
