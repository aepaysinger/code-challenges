from code_challenges.code_wars.change_it_up import ChangeItUp, changer


def test_changeitup_change_letter():
    change_it = ChangeItUp("Cat30")

    assert change_it.change_letter() == "Dbu30"


def test_changeitup_capitaliz_vowel():
    change_it = ChangeItUp("sponge1")
    change_it.change_letter()

    assert change_it.capitaliz_vowel() == "tqpOhf1"


def test_changeit_lower_consonant():
    change_it = ChangeItUp("Alice")
    change_it.change_letter()
    change_it.capitaliz_vowel()

    assert change_it.lower_consonant() == "bmjdf"


def test_changer():
    actual = changer("Hello World")
    expected = "Ifmmp xpsmE"

    assert actual == expected, f"Returned {actual} instead of {expected}"
