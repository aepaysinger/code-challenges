from code_challenges.code_wars.hamming import hamming


def test_hamming():
    actual = hamming("hamming and cheese", "Hamming and Cheese")
    expected = 2

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_hamming_same():
    actual = hamming("this is the same string", "this is the same string")
    expected = 0

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_hamming_wrong_length():
    actual = hamming("short", "long")
    expected = "The length of the string needs to be the same"

    assert actual == expected, f"Returned {actual} instead of {expected}"
