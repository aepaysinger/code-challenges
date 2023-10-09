from code_challenges.adhoc.ad_hock_challenge import (
    find_the_function,
    adding,
    even_it_up,
)


def test_find_the_function_adding():
    actual = find_the_function(
        {
            "adding": adding,
            "even_it_up": even_it_up,
        },
        "adding",
        [10, 13, 20],
    )
    expected = 43

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_find_the_function_even():
    actual = find_the_function(
        {
            "addingin": adding,
            "even_it_up": even_it_up,
        },
        "even_it_up",
        [10, 13, 20],
    )
    expected = [10, 20]

    assert actual == expected, f"Returned {actual} instead of {expected}"
