from code_challenges.hacker_rank.designer_door_mat import draw_door_mat


def test_door_mat_height_():
    actual = draw_door_mat(["7", "21"], "WELCOME")
    expected = "---------.|.---------\n------.|..|..|.------\n---.|..|..|..|..|.---\n\
-------WELCOME-------\n---.|..|..|..|..|.---\n------.|..|..|.------\n\
---------.|.---------"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_dppr_mat_even():
    actual = draw_door_mat(["6", "22"], "WELCOME")
    expected = (
        "Mat size must be N * M . (N is an odd natural number, and M is 3 times N."
    )

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_door_mat_odd_greeting():
    actual = draw_door_mat(["11", "33"], "HEY")
    expected = "---------------.|.---------------\n------------.|..|..|.------------\n---------.|..|..|..|..|.---------\n\
------.|..|..|..|..|..|..|.------\n---.|..|..|..|..|..|..|..|..|.---\n---------------HEY---------------\n\
---.|..|..|..|..|..|..|..|..|.---\n------.|..|..|..|..|..|..|.------\n---------.|..|..|..|..|.---------\n\
------------.|..|..|.------------\n---------------.|.---------------"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_door_mat_even_greeting():
    actual = draw_door_mat(["7", "21"], "HOLA")
    expected = "---------.|.---------\n------.|..|..|.------\n---.|..|..|..|..|.---\n\
---------HOLA--------\n---.|..|..|..|..|.---\n------.|..|..|.------\n---------.|.---------"

    assert actual == expected, f"Returned {actual} instead of {expected}"
