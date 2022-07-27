from code_challenges.hacker_rank.exceptions import find_the_exception


def test_find_the_exception():
    actual = find_the_exception(3, [["1", 0], ["2", "$"], ["3", "1"]])
    expected = "Error Code: integer division or modulo by zero\nError Code: invalid literal for int() with base 10: '$'\n3"

    assert actual == expected, "Returned {actual} instead of {expected}."


def test_find_the_exception_symbol_first():
    actual = find_the_exception(4, [["1", "0"], ["#", "5"], ["0", "1"], ["3", "3"]])
    expected = "Error Code: integer division or modulo by zero\nError Code: invalid literal for int() with base 10: '#'\n0\n1"

    assert actual == expected, "Returned {actual} instead of {expected}."


def test_find_the_exception_all_errors():
    actual = find_the_exception(4, [["3", "0"], ["$", "7"], ["5", "@"], ["$", "#"]])
    expected = "Error Code: integer division or modulo by zero\nError Code: invalid literal for int() with base 10: '$'\nError Code: invalid literal for int() with base 10: '@'\nError Code: invalid literal for int() with base 10: '$'"

    assert actual == expected, "Returned {actual} instead of {expected}."
