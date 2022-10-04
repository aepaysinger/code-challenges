from code_challenges.code_wars.vector_class import Vector


def test_Vector_add():
    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5])

    assert a.add(b) == Vector([4, 6, 8])


def test_Vector_subtract():
    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5])

    assert b.subtract(a) == Vector([2, 2, 2])


def test_Vector_dot():
    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5])
    #1*3 + 2*4 + 3*5 = 26
    assert a.dot(b) == 26


def test_Vector_norm():
    a = Vector([1, 2, 3])
    #sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
    assert a.norm() == 14


# def test_Vector_norm():
#     a = Vector([1, 2, 3])
#     b = Vector([3, 4, 5])
#     c = Vector([5, 6, 7, 8])
    
#     assert a.add(c) #raise an exception error