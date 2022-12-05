from code_challenges.advent_of_code.calorie_counting import get_elves_calories


def test_calorie_counting():
    actual = get_elves_calories(['1000,2000,3000', '4000', '5000,6000', '7000,8000,9000', '10000'])
    expected = 24000

    assert actual == expected, f"Returned {actual} instead of {expected}"