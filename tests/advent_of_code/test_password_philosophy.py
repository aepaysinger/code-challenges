from unittest.mock import patch


from code_challenges.advent_of_code.password_philosophy import (
    break_up_password_input,
    check_password_validity_a,
    check_password_validity_b,
)


@patch("code_challenges.advent_of_code.password_philosophy.get_password_input")
def test_break_up_password_input(get_password_input_mock):
    get_password_input_mock.return_value = [
        ["9-15", "q:", "qqnqqqqqqjqqwqqq"],
        ["3-7", "q:", "qqlqqqxq"],
        ["6-7", "z:", "zszzzgzzzzz"],
        ["3-16", "s:", "jssssrdsvsskmdssksss"],
    ]
    actual = break_up_password_input()
    expected = (
        [["9", "15"], ["3", "7"], ["6", "7"], ["3", "16"]],
        ["q", "q", "z", "s"],
        ["qqnqqqqqqjqqwqqq", "qqlqqqxq", "zszzzgzzzzz", "jssssrdsvsskmdssksss"],
    )

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.password_philosophy.get_password_input")
def test_check_password_validity_a(get_password_input_mock):
    get_password_input_mock.return_value = [
        ["9-14", "g:", "ggggggggdggggxg"],
        ["1-6", "p:", "fkpppl"],
        ["3-4", "z:", "zfzrz"],
        ["8-11", "s:", "ldsjssnmsssssgsgs"],
        ["8-9", "z:", "zzfzhxztqzzlhgl"],
        ["5-12", "n:", "pgnvncfdnnwnlkvndt"],
    ]
    actual = check_password_validity_a()
    expected = 5

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.password_philosophy.get_password_input")
def test_check_password_validity_b(get_password_input_mock):
    get_password_input_mock.return_value = [
        ["6-10", "g:", "ggzgwngggggggtqgg"],
        ["9-11", "m:", "mmmmmmrmmmmmmm"],
        ["3-4", "l:", "jlra"],
        ["8-10", "k:", "kkkfqkghbkzkkkkk"],
        ["3-7", "b:", "jwbhbhc"],
        ["4-15", "r:", "vklggxjgtgmzrlrw"],
        ["16-18", "f:", "fgnfvzxffprlpxwjrf"],
        ["5-8", "p:", "pprdhbzpp"],
        ["10-12", "r:", "rqmrkrfrkrrrrl"],
    ]
    actual = check_password_validity_b()
    expected = 6

    assert actual == expected, f"Returned {actual} instead of {expected}"
