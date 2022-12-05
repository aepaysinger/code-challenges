from code_challenges.advent_of_code.calorie_counting_pt2 import get_elves_calories_top_3


def test_calorie_counting():
    actual = get_elves_calories_top_3(['1000,2000,3000', '4000', '5000,6000', '7000,8000,9000', '10000'])
    expected = 45000

    assert actual == expected, f"Returned {actual} instead of {expected}"