from code_challenges.code_wars.find_short import find_short


def test_find_short_first():
    actual = find_short(
        "A is going to be the shortest word in this sentence and at the start."
    )
    expected = 1

    assert actual == expected, f"Should have returned {expected} instead of {actual}"


def test_find_short_middle():
    actual = find_short(
        "bsdkjfh kjhsdfjh kjhsdfhjsd khdfjh jdjj jasdlhfkjh kjshdfkh kjashdfh"
    )
    expected = 4

    assert actual == expected, f"Should have returned {expected} instead of {actual}"


def test_find_short_end():
    actual = find_short(
        "alkjhflasdfh jkhdfjhsfjkhsdf jhfjskhdaflakjsdhf kjsdahflkasdjhf ajsfhd"
    )
    expected = 6

    assert actual == expected, f"Should have returned {expected} instead of {actual}"


def test_find_short_number():
    actual = find_short("jsdhf jkshdf shjk 4jkj ssdfh 22j 33")
    expected = 2

    assert actual == expected, f"Should have returned {expected} instead of {actual}"


def test_find_short_empty_string():
    actual = find_short("")
    expected = 0

    assert actual == expected, f"Should have returned {expected} instead of {actual}"
