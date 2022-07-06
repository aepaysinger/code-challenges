import io
import sys

from code_challenges.hacker_rank.set_difference_operation import learning_difference


def test_learning_difference_result_4():
    capturedOutput = io.StringIO()                 
    sys.stdout = capturedOutput                    
    learning_difference(['1', '2', '3', '4', '5', '6', '7', '8', '9'],['10', '1', '2', '3', '11', '21', '55', '6', '8'])                                  
    sys.stdout = sys.__stdout__                     

    assert capturedOutput.getvalue() == '4\n', f"Printed: {capturedOutput.getvalue()}, instead of 4"


def test_learning_difference_result_4():
    capturedOutput = io.StringIO()                 
    sys.stdout = capturedOutput                    
    learning_difference(['9', '2', '10', '4', '8', '10', '7', '45', '9'],['7', '100', '2', '3', '11', '8', '8', '6', '8'])                                  
    sys.stdout = sys.__stdout__                     

    assert capturedOutput.getvalue() == '20\n', f"Printed: {capturedOutput.getvalue()}, instead of 4"


def test_learning_difference_result_4():
    capturedOutput = io.StringIO()                 
    sys.stdout = capturedOutput                    
    learning_difference(['1', '2', '3', '4', '5', '6', '7', '8', '9'],['10', '1', '2', '3', '11', '21', '55', '6', '8'])                                  
    sys.stdout = sys.__stdout__                     

    assert capturedOutput.getvalue() == '4\n', f"Printed: {capturedOutput.getvalue()}, instead of 4"