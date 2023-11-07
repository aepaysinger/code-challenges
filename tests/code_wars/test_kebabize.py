from code_challenges.code_wars.kebabize import kebabize


def test_kebabize_a():
    actual = kebabize("myCamelCasedString")
    expected = "my-camel-cased-string"

    assert actual == expected, f"Returned{actual} instead of {expected}."


def test_kebabize_b():
    actual = kebabize("myCamelHas3Humps")
    expected = "my-camel-has-humps"

    assert actual == expected, f"Returned{actual} instead of {expected}."


def test_kebabize_c():
    actual = kebabize("CodeWars")
    expected = "code-wars"

    assert actual == expected, f"Returned{actual} instead of {expected}."


def test_kebabize_d():
    actual = kebabize("34564")
    expected = ""

    assert actual == expected, f"Returned{actual} instead of {expected}."


def test_kebabize_e():
    actual = kebabize("SOS")
    expected = "s-o-s"

    assert actual == expected, f"Returned{actual} instead of {expected}."
