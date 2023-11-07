def how_many_cakes(recipe, available):
    if len(available) < len(recipe):
        return 0

    amount_of_cakes_per_ingredients = {}
    for key in recipe:
        if key in available:
            amount_of_cakes_per_ingredients[key] = available[key] // recipe[key]
    if amount_of_cakes_per_ingredients == {}:
        return 0
    else:
        amount_of_cakes_possible = amount_of_cakes_per_ingredients[
            list(amount_of_cakes_per_ingredients)[0]
        ]
        for key in amount_of_cakes_per_ingredients:
            if amount_of_cakes_per_ingredients[key] < amount_of_cakes_possible:
                amount_of_cakes_possible = amount_of_cakes_per_ingredients[key]
    if len(recipe) != len(amount_of_cakes_per_ingredients):
        return 0

    return amount_of_cakes_possible


if __name__ == "__main__":
    recipe = {"eggs": 98, "chocolate": 12, "apples": 44}
    available = {
        "chocolate": 6919,
        "sugar": 4692,
        "milk": 3500,
        "butter": 1485,
        "crumbles": 1543,
        "cream": 9535,
        "flour": 4280,
        "cocoa": 9788,
        "pears": 3562,
        "oil": 6589,
    }
    print(how_many_cakes(recipe, available))
