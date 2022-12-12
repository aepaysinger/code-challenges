from unittest.mock import patch

from code_challenges.advent_of_code.calorie_counting import get_elves_calories


@patch("code_challenges.advent_of_code.calorie_counting.get_elves_calories")
def test_get_elves_calories(get_elves_calories_mock):
    get_elves_calories_mock.return_value = ['1000,2000,3000', '4000', '5000,6000', '7000,8000,9000', '10000']
    # expected = 24000

    assert get_elves_calories() == 24000