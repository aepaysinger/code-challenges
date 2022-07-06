import io
import sys

from code_challenges.hacker_rank.collections_counter import rhagu_shoe_orders


def test_collections_counter_a():
    capturedOutput = io.StringIO()                 
    sys.stdout = capturedOutput                     
    rhagu_shoe_orders(['2', '3', '4', '5', '6', '8', '7', '6', '5', '18'],[['6', '55'], ['6', '45'], ['6', '55'], ['4', '40'], ['18', '60'], ['10', '50']])                                  
    sys.stdout = sys.__stdout__                    

    assert capturedOutput.getvalue() == '200\n', f"Printed: {capturedOutput.getvalue()}, instead of 200"


def test_collections_counter_b():
    capturedOutput = io.StringIO()                 
    sys.stdout = capturedOutput                     
    rhagu_shoe_orders(['3', '9', '6', '9', '3', '8', '7', '12', '4', '18'],[['5', '25'], ['6', '36'], ['9', '81'], ['4', '16'], ['18', '60'], ['10', '50']])                                  
    sys.stdout = sys.__stdout__                    

    assert capturedOutput.getvalue() == '193\n', f"Printed: {capturedOutput.getvalue()}, instead of 193"  


def test_collections_counter_c():
    capturedOutput = io.StringIO()                 
    sys.stdout = capturedOutput                     
    rhagu_shoe_orders(['9', '9', '9', '9', '9'],[['6', '55'], ['9', '45'], ['6', '55'], ['9', '40'], ['18', '60'], ['10', '50']])                                  
    sys.stdout = sys.__stdout__                    

    assert capturedOutput.getvalue() == '85\n', f"Printed: {capturedOutput.getvalue()}, instead of 85"  