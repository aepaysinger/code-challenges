from unittest.mock import patch

from code_challenges.advent_of_code.calorie_counting import get_elves_calories


@patch("code_challenges.advent_of_code.calorie_counting.elves_input")
def test_get_elves_calories_a(elves_input_mock):
    elves_input_mock.return_value = [
        "1000,2000,3000",
        "4000",
        "5000,6000",
        "7000,8000,9000",
        "10000",
    ]
    actual = get_elves_calories()
    expected = 24000

    assert actual == expected


@patch("code_challenges.advent_of_code.calorie_counting.elves_input")
def test_get_elves_calories_b(elves_input_mock):
    elves_input_mock.return_value = [
        "1000,3000",
        "40,700",
        "5,70,900,6000",
        "7087",
        "10000",
    ]
    actual = get_elves_calories()
    expected = 10000

    assert actual == expected


@patch("code_challenges.advent_of_code.calorie_counting.elves_input")
def test_get_elves_calories_c(elves_input_mock):
    elves_input_mock.return_value = [
        "754645,4534,223,567",
        "40,163,72,35",
        "50,56443500,6000",
        "700080009000",
        "10000",
    ]
    actual = get_elves_calories()
    expected = 700080009000

    assert actual == expected
