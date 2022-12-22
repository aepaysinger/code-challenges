from code_challenges.hacker_rank.weird_or_not_weird import weird_or_not_weird


def test_weird():
    actual = weird_or_not_weird(5)
    expected = "Weird"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_not_weird():
    actual = weird_or_not_weird(4)
    expected = "Not Weird"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_weird_a():
    actual = weird_or_not_weird(8)
    expected = "Weird"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_not_weird_a():
    actual = weird_or_not_weird(24)
    expected = "Not Weird"

    assert actual == expected, f"Returned {actual} instead of {expected}"
