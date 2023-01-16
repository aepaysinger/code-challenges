from code_challenges.code_wars.camel_case import CamelCase, camel_case


def test_camelcase_change_case():
    camel_it = CamelCase("hello world")

    assert camel_it.change_case() == ["Hello", "World"]


def test_camelcase_make_string_camel_case():
    camel_it = CamelCase(" camel case word")

    assert camel_it.make_string_camel_case() == "CamelCaseWord"


def test_camel_case():
    actual = camel_case("test this out")
    expected = "TestThisOut"

    assert actual == expected, f"Returned {actual} instead of {expected}"
