from unittest.mock import patch


from code_challenges.advent_of_code.calorie_counting_pt2 import get_elves_calories_top_3


@patch("code_challenges.advent_of_code.calorie_counting_pt2.elves_input")
def test_get_elves_calories_top_3_a(elves_input_mock):
    elves_input_mock.return_value = [
        "1000,2000,3000",
        "4000",
        "5000,6000",
        "7000,8000,9000",
        "10000",
    ]
    actual = get_elves_calories_top_3()
    expected = 45000

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.calorie_counting_pt2.elves_input")
def test_get_elves_calories_top_3_b(elves_input_mock):
    elves_input_mock.return_value = [
        "1000,3000",
        "40,700",
        "5,70,900,6000",
        "7087",
        "10000",
    ]
    actual = get_elves_calories_top_3()
    expected = 24062

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.calorie_counting_pt2.elves_input")
def test_get_elves_calories_top_3_c(elves_input_mock):
    elves_input_mock.return_value = [
        "754645,4534,223,567",
        "40,163,72,35",
        "50,56443500,6000",
        "700080009000",
        "10000",
    ]
    actual = get_elves_calories_top_3()
    expected = 700137218519

    assert actual == expected, f"Returned {actual} instead of {expected}"
