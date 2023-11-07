import itertools


def get_expense_report():
    with open("./code_challenges/advent_of_code/expense_report_input") as numbers:
        expnse_report = numbers.read().split("\n")

    return [int(number) for number in expnse_report]


def find_sum_then_multiply_2():
    expense_report = get_expense_report()
    for numbers in itertools.combinations(expense_report, 2):
        if sum(numbers) == 2020:
            return numbers[0] * numbers[1]


def find_sum_then_multiply_3():
    expense_report = get_expense_report()
    for numbers in itertools.combinations(expense_report, 3):
        if sum(numbers) == 2020:
            return numbers[0] * numbers[1] * numbers[2]
