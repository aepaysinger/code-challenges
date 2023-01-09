from code_challenges.code_wars.order_strings import OrderStrings, order


# def test_orderstrings_find_the_number():
#     change_order = OrderStrings("is2 Thi1s T4est 3a")
#     change_order.find_the_number()

#     assert change_order.position_in_string == {0: 1, 1: 0, 2: 3, 3: 2}


# def test_orderstrings_build_updated_order_strings():
#     change_order = OrderStrings("is2 Thi1s T4est 3a")
#     change_order.find_the_number()

#     assert change_order.build_updated_order_string() == "Thi1s is2 3a T4est"


def test_orderstrings_find_position():
    change_order = OrderStrings("is2 Thi1s T4est 3a")

    assert change_order.find_position("is2") == 2


def test_orderstrings_sort_text():
    change_order = OrderStrings("is2 Thi1s T4est 3a")

    assert change_order.sort_text() == "Thi1s is2 3a T4est"


def test_order():
    actual = order("4of Fo1r pe6ople g3ood th5e the2")
    expected = "Fo1r the2 g3ood 4of th5e pe6ople"

    assert actual == expected, f"Returned {actual} instead of {expected}"
