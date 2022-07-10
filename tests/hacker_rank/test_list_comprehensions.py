import io
import sys

from code_challenges.hacker_rank.list_comprehensions import create_cuboids


def test_create_cuboids_n2():
    capturedOutput = io.StringIO()                  
    sys.stdout = capturedOutput                     
    create_cuboids(1, 1, 1, 2)                                  
    sys.stdout = sys.__stdout__                    

    assert capturedOutput.getvalue() == '[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]\n', f"Printed: {capturedOutput.getvalue()}, instead of [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]"


def test_create_cuboids_n1():
    capturedOutput = io.StringIO()                  
    sys.stdout = capturedOutput                     
    create_cuboids(2, 2, 1, 1)                                  
    sys.stdout = sys.__stdout__                    

    assert capturedOutput.getvalue() == '[[0, 0, 0], [0, 1, 1], [0, 2, 0], [0, 2, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1], [1, 2, 0], [1, 2, 1], [2, 0, 0], [2, 0, 1], [2, 1, 0], [2, 1, 1], [2, 2, 0], [2, 2, 1]]\n', f"Printed: {capturedOutput.getvalue()}, instead of [[0, 0, 0], [0, 1, 1], [0, 2, 0], [0, 2, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1], [1, 2, 0], [1, 2, 1], [2, 0, 0], [2, 0, 1], [2, 1, 0], [2, 1, 1], [2, 2, 0], [2, 2, 1]]"


def test_create_cuboids_n3():
    capturedOutput = io.StringIO()                  
    sys.stdout = capturedOutput                     
    create_cuboids(1, 3, 1, 3)                                  
    sys.stdout = sys.__stdout__                    

    assert capturedOutput.getvalue() == '[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [0, 2, 0], [0, 3, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 2, 1], [1, 3, 0], [1, 3, 1]]\n', f"Printed: {capturedOutput.getvalue()}, instead of [[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [0, 2, 0], [0, 3, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 2, 1], [1, 3, 0], [1, 3, 1]]"    
    