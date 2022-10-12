from code_challenges.code_wars.instance import Vehicle, Planet, show_me


def test_vehicle():
    porsche = Vehicle(2, 4, "Gas")

    assert porsche.seats == 2
    assert porsche.wheels == 4
    assert porsche.engine == "Gas"
    assert (
        show_me(porsche)
        == "Hi, I'm one of those Vehicles! Have a look at my engine, seats and wheels."
    )


def test_planet():
    earth = Planet("moon")

    assert show_me(earth) == "Hi, I'm one of those Planets! Have a look at my moon."
