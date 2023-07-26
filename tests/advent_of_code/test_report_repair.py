from unittest.mock import patch

from code_challenges.advent_of_code.report_repair import (
    find_sum_then_multiply_2,
    find_sum_then_multiply_3,
)


@patch("code_challenges.advent_of_code.report_repair.get_expense_report")
def test_find_sum_then_multiply_2(expense_report_input_mock):
    expense_report_input_mock.return_value = [1721, 979, 366, 299, 675, 1456]
    actual = find_sum_then_multiply_2()
    expected = 514579

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.report_repair.get_expense_report")
def test_find_sum_then_multiply_3(expense_report_input_mock):
    expense_report_input_mock.return_value = [1721, 979, 366, 299, 675, 1456]
    actual = find_sum_then_multiply_3()
    expected = 241861950

    assert actual == expected, f"Returned {actual} instead of {expected}"
