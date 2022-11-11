from code_challenges.code_wars.barista_manager import coffee_wait


def test_coffee_wait_1_machine():
    actual = coffee_wait([2,3,4], 1)
    expected = 22

    assert actual == expected, f"Return {actual} instead of {expected}"


def test_coffee_wait_2_machines():
    actual = coffee_wait([2,3,4], 2)
    expected = 13

    assert actual == expected, f"Return {actual} instead of {expected}"


def test_coffee_wait_3_machines():
    actual = coffee_wait([2,3,4], 3)
    expected = 9

    assert actual == expected, f"Return {actual} instead of {expected}"


def test_coffee_wait_no_orders():
    actual = coffee_wait([], 1)
    expected = 0

    assert actual == expected, f"Return {actual} instead of {expected}"