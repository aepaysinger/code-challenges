from code_challenges.code_wars.phone_words import Phone
from code_challenges.code_wars.phone_words import phone_code


def test_translate_numbers_spaces():
    secret_code = Phone()

    assert secret_code.translate_numbers("000") == "   "


def test_translate_numbers_1():
    secret_code = Phone()

    assert secret_code.translate_numbers("22128") == "bat"


def test_translate_numbers_same_letter():
    secret_code = Phone()

    assert secret_code.translate_numbers("4433555555666") == "hello"


def test_phone_code():
    actual = phone_code("3399997772")
    expected = "ezra"

    assert actual == expected, f"Returned {actual} instead of {expected}"
