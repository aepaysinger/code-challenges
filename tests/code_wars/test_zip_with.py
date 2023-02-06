from operator import add, sub, mul


from code_challenges.code_wars.zip_with import ZipWith, zip_with


def test_zipwith():
    zipping = ZipWith(add, [0, 1, 2, 3, 4, 5], [6, 5, 4, 3, 2, 1])

    assert zipping.zip_with() == [6, 6, 6, 6, 6, 6]


def test_zip_with_sub():
    actual = zip_with(sub, [0, 1, 2, 3, 4, 5], [6, 5, 4, 3, 2, 1])
    expected = [-6, -4, -2, 0, 2, 4]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_zip_with_mul():
    actual = zip_with(mul, ["a", "b", "c", "d", "e", "f"], [6, 5, 4, 3, 2, 1])
    expected = ["aaaaaa", "bbbbb", "cccc", "ddd", "ee", "f"]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_zip_with_pow():
    actual = zip_with(pow, [10, 10, 10, 10], [0, 1, 2, 3])
    expected = [1, 10, 100, 1000]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_zip_with_max():
    actual = zip_with(max, [1, 4, 7, 1, 4, 7], [4, 7, 1, 4, 7, 1])
    expected = [4, 7, 7, 4, 7, 7]

    assert actual == expected, f"Returned {actual} instead of {expected}"
