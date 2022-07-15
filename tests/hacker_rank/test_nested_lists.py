from code_challenges.hacker_rank.nested_lists import student_grades


def test_nested_lists_tie():
    actual = student_grades(
        [
            ["Harry", 37.21],
            ["Berry", 37.21],
            ["Tina", 37.2],
            ["Akriti", 41.0],
            ["Harsh", 39.0],
        ]
    )
    expected = "Berry\nHarry"

    assert actual == expected, f"returned {actual} instead of {expected}"


def test_nested_lists():
    actual = student_grades([["Ezra", 98.0], ["Oliver", 96.7], ["Rusty", 55.7]])
    expected = "Oliver"

    assert actual == expected, f"returned {actual} instead of {expected}"


def test_nested_lists_no_second_lowest():
    actual = student_grades(
        [["Bob", 65.4], ["Mandy", 65.4], ["Lemon", 65.4], ["Frank", 65.4]]
    )
    expected = "No Second Lowest"

    assert actual == expected, f"returned {actual} instead of {expected}"
