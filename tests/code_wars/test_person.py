from code_challenges.code_wars.person import Person


def test_person_full_name():
    person = Person("Yukihiro", "Matsumoto", 47)

    assert person.full_name == "Yukihiro Matsumoto"
    assert person.age == 47


def test_person_first_last_name():
    person = Person("Benjamin", "Bunny", 300)

    assert person.first_name == "Benjamin"
    assert person.last_name == "Bunny"
    assert person.full_name == "Benjamin Bunny"
    assert person.age == 300
