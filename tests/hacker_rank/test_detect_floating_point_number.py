from code_challenges.hacker_rank.detect_floating_point_number import (
    detect_floating_point_number,
)


def test_string_with_letters():
    actual = detect_floating_point_number(
        [".41M4", "+1.54OO468", "4.878253", ".73937", "+O.O1"]
    )
    expected = "False\nFalse\nTrue\nTrue\nFalse"

    assert (
        actual == expected
    ), f"Should have returned {expected}, but returned {actual}. Make sure you are accounting for letters in the middle."


def test_string_with_positive_and_negative():
    actual = detect_floating_point_number(
        ["+3.35567", "-976.676", "++54.444", "+8753", "-8754"]
    )
    expected = "True\nTrue\nFalse\nFalse\nFalse"

    assert (
        actual == expected
    ), f"positive and negative signs should be dropped at the beginning but if they are anywhere else it should return False."


def test_string_with_multiple_decimals():
    actual = detect_floating_point_number(
        [".454.454.454", "0.3434", "23432.45", ".45.3432.2"]
    )
    expected = "False\nTrue\nTrue\nFalse"

    assert actual == expected, "floats should have only one decimal point."
