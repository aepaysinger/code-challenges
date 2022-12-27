from code_challenges.code_wars.remove_parentheses import (
    CharacterRemover,
    remove_parentheses,
)


def test_charachter_remover_item_to_remove():
    characters = CharacterRemover("this(is)it")

    assert characters.item_to_remove() == (4, 7)


def test_character_remover_item_to_remove_2():
    characters = CharacterRemover("a(b)c(d)")

    assert characters.item_to_remove() == (1, 3)


def test_character_remover_remove_item():
    characters = CharacterRemover("this(is)it")
    characters.item_to_remove()

    assert characters.remove_item() == "thisit"


def test_charcter_remover_remove_item_2():
    characters = CharacterRemover("a(b)c(d)")
    characters.item_to_remove()

    assert characters.remove_item() == "ac"


def test_remove_parentheses():
    actual = remove_parentheses("hey(um) you(guy)!")
    expected = "hey you!"

    assert actual == expected, f"Returned {actual} instead of {expected}"
