from code_challenges.hacker_rank.validating_phone_numbers import check_for_mobile_number


def test_check_for_mobile_number():
    actual = check_for_mobile_number(
        ["52021597954", "7458907623", "8954762314", "8745321596"]
    )
    expected = "NO\nYES\nYES\nYES"

    assert actual == expected, "Returned {actual} instead of {expected}"


def test_check_for_mobile_too_short():
    actual = check_for_mobile_number(
        ["520217954", "7458907623", "8952314", "8745321596"]
    )
    expected = "NO\nYES\nNO\nYES"

    assert actual == expected, "Returned {actual} instead of {expected}"


def test_check_for_mobile_not_digit():
    actual = check_for_mobile_number(
        ["7543H0864", ".458907623", "jutrdcgyu", "8745321596"]
    )
    expected = "NO\nNO\nNO\nYES"

    assert actual == expected, "Returned {actual} instead of {expected}"
