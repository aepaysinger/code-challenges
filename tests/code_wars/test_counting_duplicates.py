from code_challenges.code_wars.counting_duplicates import counting_duplicates


def test_counting_duplicates():
    actual = counting_duplicates("aajjjuu2blk48herrsa")
    expected = 4

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_counting_duplicates_upper_and_lower():
    actual = counting_duplicates("Phfbj8A0a")
    expected = 1

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_counting_duplicates_all_numbers():
    actual = counting_duplicates("23542356564")
    expected = 5

    assert actual == expected, f"Returned {actual} instead of {expected}"
