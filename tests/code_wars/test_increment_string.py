from code_challenges.code_wars.increment_string import increment_string


def test_increment_string_basic():
    actual = increment_string("foo")
    expected = "foo1"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_increment_string_zero_first():
    actual = increment_string("foo001")
    expected = "foo002"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_increment_string_double_digits():
    actual = increment_string("foobar99")
    expected = "foobar100"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_increment_string_tricky():
    actual = increment_string("foobar099")
    expected = "foobar100"

    assert actual == expected, f"Returned {actual} instead of {expected}"
