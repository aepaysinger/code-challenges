from code_challenges.code_wars.decipher_this import decipher_this


def test_decipher_this_numbers():
    actual = decipher_this("65 65 65")
    expected = "A A A"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_decipher_this_one_letter():
    actual = decipher_this("105n 97n 104e 98e")
    expected = "in an he be"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_decipher_this_two_letters():
    actual = decipher_this("115wa 111dl 111lw")
    expected = "saw old owl"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_decipher_this_three_and_more_mix():
    actual = decipher_this("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare")
    expected = "The less he spoke the more he heard"

    assert actual == expected, f"Returned {actual} instead of {expected}"
