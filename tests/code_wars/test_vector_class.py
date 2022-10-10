import math, pytest

from code_challenges.code_wars.vector_class import Vector


def test_vector_add():
    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5])

    assert a.add(b) == Vector([4, 6, 8])


def test_vector_add_wrong_length():
    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5, 7])
    with pytest.raises(ValueError) as excinfo:
        a.add(b)

    assert str(excinfo.value) == "Vectors must be the same length"


def test_vector_subtract():
    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5])

    assert b.subtract(a) == Vector([2, 2, 2])


def test_vector_subtract_wrong_length():
    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5, 7])
    with pytest.raises(ValueError) as excinfo:
        b.subtract(a)

    assert str(excinfo.value) == "Vectors must be the same length"


def test_vector_dot():
    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5])
    # 1*3 + 2*4 + 3*5 = 26
    assert a.dot(b) == 26


def test_vector_dot_wrong_length():
    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5, 7])
    with pytest.raises(ValueError) as excinfo:
        a.dot(b)

    assert str(excinfo.value) == "Vectors must be the same length"


def test_vector_norm():
    a = Vector([1, 2, 3])
    # sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
    # 1+4+9
    assert a.norm() == math.sqrt(14)


def test_vector_str():
    a = Vector([1, 2, 3])

    assert str(a) == "(1,2,3)"


def test_vector_tostring():
    a = Vector([1, 2, 3])

    assert str(a) == "(1,2,3)"
