from code_challenges.code_wars.persistent_bugger import (
    PersistentMultiplication,
    persistence,
)


def test_persistent_multiplication_break_up_numbers():
    persistent_numbers = PersistentMultiplication(248)

    assert persistent_numbers.break_up_numbers() == [2, 4, 8]


def test_persistent_multiplication_mulitply_numbers():
    persistent_numbers = PersistentMultiplication(999)
    persistent_numbers.break_up_numbers()

    assert persistent_numbers.multiply_numbers() == 4


def test_persistence():
    actual = persistence(25)
    expected = 2

    assert actual == expected, f"Returned {actual} instead of {expected}"
