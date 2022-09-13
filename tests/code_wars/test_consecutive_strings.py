from code_challenges.code_wars.consecutive_strings import consecutive_strings


def test_consecutive_strings_2():
    actual = consecutive_strings(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
    expected = "abigailtheta"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_consecutive_strings_3():
    actual = consecutive_strings(["zone", "abigail", "theta", "form", "libe", "zas"], 3)
    expected = "zoneabigailtheta"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_consecutive_strings_same_length():
    actual = consecutive_strings(["auto", "zone", "love", "them", "cars", "man!"], 2)
    expected = "autozone"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_consecutive_strings_k_bigger():
    actual = consecutive_strings(["auto", "zone", "love", "them", "cars", "man!"], 7)
    expected = ""

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_consecutive_strings_k_too_small():
    actual = consecutive_strings(["auto", "zone", "love", "them", "cars", "man!"], -3)
    expected = ""

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_consecutive_strings_len_0():
    actual = consecutive_strings([], 2)
    expected = ""

    assert actual == expected, f"Returned {actual} instead of {expected}"
