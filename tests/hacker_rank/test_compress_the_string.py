from code_challenges.hacker_rank.compress_the_string import compressing_strings


def test_compressing_strings_letters():
    actual = compressing_strings("aabbbcaafff")
    expected = "(2, a) (3, b) (1, c) (2, a) (3, f)"

    assert actual == expected, f"Returned: {actual}, instead of {expected}"


def test_compressing_strings_numbers():
    actual = compressing_strings("1113338844331")
    expected = "(3, 1) (3, 3) (2, 8) (2, 4) (2, 3) (1, 1)"

    assert actual == expected, f"Returned: {actual}, instead of {expected}"


def test_compressing_strings_letter_and_numbers():
    actual = compressing_strings("aa888n333dddd")
    expected = "(2, a) (3, 8) (1, n) (3, 3) (4, d)"

    assert actual == expected, f"Returned: {actual}, instead of {expected}"
