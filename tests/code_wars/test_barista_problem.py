from code_challenges.code_wars.barista_problem import fastest_coffee_orders


def test_fastest_coffee_orders_a():
    actual = fastest_coffee_orders([2, 10, 5, 3, 9])
    expected = 85

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_fastest_coffee_orders_b():
    actual = fastest_coffee_orders([4, 3, 2])
    expected = 22

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_fastest_coffee_orders_None():
    actual = fastest_coffee_orders([])
    expected = 0

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_fastest_coffee_orders_c():
    actual = fastest_coffee_orders([20, 5])
    expected = 32

    assert actual == expected, f"Returned {actual} instead of {expected}"
