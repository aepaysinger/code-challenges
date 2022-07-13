from code_challenges.hacker_rank.list_comprehensions import create_cuboids


def test_create_cuboids_n2():                    
    actual = create_cuboids(1, 1, 1, 2)                                                   

    assert actual == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]], f"Returned: {actual}, instead of [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]"


def test_create_cuboids_n1():                  
    actual = create_cuboids(2, 2, 1, 1)                                                     

    assert actual == [[0, 0, 0], [0, 1, 1], [0, 2, 0], [0, 2, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1], [1, 2, 0], [1, 2, 1], [2, 0, 0], [2, 0, 1], [2, 1, 0], [2, 1, 1], [2, 2, 0], [2, 2, 1]], f"Printed: {actual}, instead of [[0, 0, 0], [0, 1, 1], [0, 2, 0], [0, 2, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1], [1, 2, 0], [1, 2, 1], [2, 0, 0], [2, 0, 1], [2, 1, 0], [2, 1, 1], [2, 2, 0], [2, 2, 1]]"


def test_create_cuboids_n3():                  
    actual = create_cuboids(1, 3, 1, 3)                                                     

    assert actual == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [0, 2, 0], [0, 3, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 2, 1], [1, 3, 0], [1, 3, 1]], f"Printed: {actual}, instead of [[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [0, 2, 0], [0, 3, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 2, 1], [1, 3, 0], [1, 3, 1]]"    
