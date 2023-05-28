from code_challenges.code_wars.n_point_crossover import crossover


def test_crossover_0():
    actual = crossover([], [1, 2, 3], [4, 5, 6])
    expected = [1, 2, 3], [4, 5, 6]
    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_crossover_1():
    actual = crossover([1], ["a", "b", "c"], ["x", "y", "z"])
    expected = ["a", "y", "z"], ["x", "b", "c"]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_crossover_2():
    actual = crossover([1, 3], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2])
    expected = [1, 2, 2, 1, 1], [2, 1, 1, 2, 2]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_crossover_3():
    actual = crossover(
        [1, 3, 5], ["a", "b", "c", "d", "e", "f", "g"], [1, 1, 1, 1, 1, 1, 1]
    )
    expected = ["a", 1, 1, "d", "e", 1, 1], [1, "b", "c", 1, 1, "f", "g"]

    assert actual == expected, f"Returned {actual} instead of {expected}"
