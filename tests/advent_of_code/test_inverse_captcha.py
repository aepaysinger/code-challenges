from unittest.mock import patch


from code_challenges.advent_of_code.inverse_captcha import check_to_add_next_digit, check_to_add_halfway_digit


@patch("code_challenges.advent_of_code.inverse_captcha.digits_input")
def test_check_to_add_next_digit_a(digits_input_mock):
    digits_input_mock.return_value = [9, 1, 2, 1, 2, 1, 2, 9]
    actual = check_to_add_next_digit()
    expected = 9

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.inverse_captcha.digits_input")
def test_check_to_add_next_digit_b(digits_input_mock):
    digits_input_mock.return_value = [1, 1, 2, 2]
    actual = check_to_add_next_digit()
    expected = 3

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.inverse_captcha.digits_input")
def test_check_to_add_halfway_digit_a(digits_input_mock):
    digits_input_mock.return_value = [1, 2, 3, 1, 2, 3]
    actual = check_to_add_halfway_digit()
    expected = 12

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.inverse_captcha.digits_input")
def test_check_to_add_halfway_digit_b(digits_input_mock):
    digits_input_mock.return_value = [1, 2, 2, 1]
    actual = check_to_add_halfway_digit()
    expected = 0

    assert actual == expected, f"Returned {actual} instead of {expected}"