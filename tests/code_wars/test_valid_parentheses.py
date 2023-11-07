from code_challenges.code_wars.valid_parentheses import valid_parentheses


def test_valid_parentheses_a():
    actual = valid_parentheses("  (")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_valid_parentheses_b():
    actual = valid_parentheses(")test")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_valid_parentheses_c():
    actual = valid_parentheses("")
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_valid_parentheses_d():
    actual = valid_parentheses("hi(hi)()")
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_valid_parentheses_e():
    actual = valid_parentheses("hi())(")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_valid_parentheses_f():
    actual = valid_parentheses("((())")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_valid_parentheses_g():
    actual = valid_parentheses("(((())")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"
