from code_challenges.adhoc.substring import LookUp


def test_lookup_find_in():
    original = LookUp("the quick red fox")

    assert original.find("red") == 10


def test_lookup_find_out():
    original = LookUp("the quick red fox")

    assert original.find("blue") == -1


def test_lookup_find_end():
    original = LookUp("the quick red fox")

    assert original.find("fox") == 14
