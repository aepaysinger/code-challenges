from code_challenges.code_wars.cakes import how_many_cakes


def test_how_many_cakes_recipe_bigger_than_available():
    actual = how_many_cakes(
        {"flour": 500, "sugar": 200, "eggs": 1, "vanilla": 3},
        {"flour": 3000, "sugar": 1200, "eggs": 5},
    )
    expected = 0

    assert (
        actual == expected
    ), f"Returned {actual} insted of {expected}, missing ingredients in recipe"


def test_how_many_cakes_available_bigger_than_recipe():
    actual = how_many_cakes(
        {"flour": 500, "sugar": 200, "eggs": 1, "vanilla": 3},
        {
            "flour": 3000,
            "sugar": 1200,
            "eggs": 5,
            "vanilla": 6,
            "cinnamon": 10,
            "ginger": 20,
        },
    )
    expected = 2

    assert actual == expected, f"Returned {actual} insted of {expected}"


def test_how_many_cakes_no_ingredients_match():
    actual = how_many_cakes(
        {
            "flour": 500,
            "sugar": 200,
            "eggs": 1,
        },
        {
            "water": 6,
            "apples": 20,
            "nutmeg": 3,
            "vanilla": 2,
            "cinnamon": 10,
            "ginger": 20,
        },
    )
    expected = 0

    assert actual == expected, f"Returned {actual} insted of {expected}"
