from code_challenges.hacker_rank.write_a_function import is_leap


def test_is_leap_2000_true():
    actual = is_leap(2000)

    assert actual == True, f"Returned: {actual}, instead of True"


def test_is_leap_1900_false():
    actual = is_leap(1900)

    assert actual == False, f"Returned: {actual}, instead of False"


def test_is_leap_2016_true():
    actual = is_leap(2016)

    assert actual == True, f"Returned: {actual}, instead of True"
