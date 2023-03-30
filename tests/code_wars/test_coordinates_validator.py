from code_challenges.code_wars.coordinates_validator import is_valid_coordinates


def test_is_valid_coordinates_a():
    actual = is_valid_coordinates("2342.43536, 34.324236")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_is_valid_coordinates_b():
    actual = is_valid_coordinates("N23.43345, E32.6457")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_is_valid_coordinates_c():
    actual = is_valid_coordinates("23.245, 1e1")
    expected = False

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_is_valid_coordinates_d():
    actual = is_valid_coordinates("24.53525235, 23.45235")
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_is_valid_coordinates_e():
    actual = is_valid_coordinates("29, 90")
    expected = True

    assert actual == expected, f"Returned {actual} instead of {expected}"
