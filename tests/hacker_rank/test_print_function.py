from code_challenges.hacker_rank.print_function import count_up


def test_count_up_4():
    actual = count_up(4)

    assert actual == '1234', f"Printed: {actual}, instead of 1234"


def test_count_up_8():
    actual = count_up(8)

    assert actual == '12345678', f"Printed: {actual}, instead of 12345678"


def test_count_up_1():
    actual = count_up(1)

    assert actual == '1', f"Printed: {actual}, instead of 1"