from code_challenges.code_wars.skills_master import count_skills


def test_count_skills_empty():
    actual = count_skills([0, 0, 0, 1, 3, 3, 2], set())
    expected = 0

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_count_skills_single():
    actual = count_skills([0, 0, 0, 1, 3, 3, 2], {2})
    expected = 2

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_count_skills_two():
    actual = count_skills([0, 0, 0, 1, 3, 3, 2], {3, 6})
    expected = 5

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_count_skills_two():
    actual = count_skills([0, 0, 0, 1, 3, 3, 2], {1, 2, 3, 4, 5, 6})
    expected = 7

    assert actual == expected, f"Returned {actual} instead of {expected}"
