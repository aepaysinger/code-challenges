from itertools import combinations

from code_challenges.hacker_rank.iterables_and_iterators import (
    chances_of_finding_the_letter_a,
)


def test_chances_of_finding_the_letter_a_2():
    actual = chances_of_finding_the_letter_a(["a", "a", "c", "d"], 2)
    expected = 0.8333

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_chances_of_finding_the_letter_a_3():
    actual = chances_of_finding_the_letter_a(
        [
            "b",
            "a",
            "a",
            "c",
            "d",
            "a",
        ],
        3,
    )
    expected = 0.95

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_chances_of_finding_the_letter_a_no_a():
    actual = chances_of_finding_the_letter_a(["b", "c", "b", "c", "d", "d"], 2)
    expected = 0

    assert actual == expected, f"Returned {actual} instead of {expected}"
