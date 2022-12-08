from code_challenges.code_wars.phone_words import Phone
from code_challenges.code_wars.phone_words import phone_code


def test_translate_numbers_spaces():
    secret_code = Phone("000")

    assert secret_code.translate_numbers() == "   "


def test_translate_numbers_1():
    secret_code = Phone("22128")

    assert secret_code.translate_numbers() == "bat"


def test_translate_numbers_same_letter():
    secret_code = Phone("4433555555666")

    assert secret_code.translate_numbers() == "hello"


def test_phone_code():
    actual = phone_code("3399997772")
    expected = "ezra"

    assert actual == expected, f"Returned {actual} instead of {expected}"
