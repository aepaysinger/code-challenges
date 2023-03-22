from code_challenges.code_wars.unique_in_order import UniqueOrder, unique_in_order


def test_unique_order():
    find_unique_order = UniqueOrder("AAAABBBCCDAABBB")

    assert find_unique_order.pull_out_unique_character() == [
        "A",
        "B",
        "C",
        "D",
        "A",
        "B",
    ]


def test_unique_in_order_upper_and_lower():
    actual = unique_in_order("ABBCcAD")
    expected = ["A", "B", "C", "c", "A", "D"]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_unique_in_order_numbers():
    actual = unique_in_order([1, 2, 2, 3, 3])
    expected = [1, 2, 3]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_unique_in_order_string_and_int():
    actual = unique_in_order(["A", 1, 1, "a", 3, "B", "B"])
    expected = ["A", 1, "a", 3, "B"]

    assert actual == expected, f"Returned {actual} instead of {expected}"
