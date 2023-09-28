from code_challenges.code_wars.find_the_time import what_time_is_it


def test_what_time_is_it_a():
    actual = what_time_is_it(180)
    expected = "06:00"

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_what_time_is_it_b():
    actual = what_time_is_it(105)
    expected = "03:30"

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_what_time_is_it_c():
    actual = what_time_is_it(0)
    expected = "12:00"

    assert actual == expected, f"Returned {actual} instead of {expected}."


def test_what_time_is_it_d():
    actual = what_time_is_it(163.347)
    expected = "05:26"

    assert actual == expected, f"Returned {actual} instead of {expected}."
