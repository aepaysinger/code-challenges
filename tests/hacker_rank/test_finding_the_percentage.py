from code_challenges.hacker_rank.finding_the_percentage import finding_the_percentage


def test_finding_the_percentage():
    actual = finding_the_percentage(
        {
            "Krishna": [67.0, 68.0, 69.0],
            "Arjun": [70.0, 98.0, 63.0],
            "Malika": [52.0, 56.0, 60.0],
        },
        "Malika",
    )
    expected = "56.00"

    assert actual == expected, f"Returned {actual} instead of {expected}"
