from code_challenges.code_wars.multiplication_table import (
    MultiplicationTable,
    multiplication_table,
)


def test_build_table_3():
    the_table = MultiplicationTable(3)

    assert the_table.build_table() == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


def test_multiplication_table_5():
    actual = multiplication_table(5)
    expected = [
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8, 10],
        [3, 6, 9, 12, 15],
        [4, 8, 12, 16, 20],
        [5, 10, 15, 20, 25],
    ]

    assert actual == expected, f"Returned {actual} instead of {expected}"
