import io
import sys

from code_challenges.hacker_rank.compress_the_string import compressing_strings


def test_compressing_strings_letters():
    capturedOutput = io.StringIO()                 
    sys.stdout = capturedOutput                    
    compressing_strings("aabbbcaafff")                                  
    sys.stdout = sys.__stdout__                     

    assert capturedOutput.getvalue() == "(2, a) (3, b) (1, c) (2, a) (3, f)", f"Printed: {capturedOutput.getvalue()}, instead of (2, a) (3, b) (1, c) (2, a) (3, f)"


def test_compressing_strings_numbers():
    capturedOutput = io.StringIO()                 
    sys.stdout = capturedOutput                    
    compressing_strings("1113338844331")                                  
    sys.stdout = sys.__stdout__                     

    assert capturedOutput.getvalue() == "(3, 1) (3, 3) (2, 8) (2, 4) (2, 3) (1, 1)", f"Printed: {capturedOutput.getvalue()}, instead of (3, 1) (3, 3) (2, 8) (2, 4) (2, 3) (1, 1)"   


def test_compressing_strings_letter_and_numbers():
    capturedOutput = io.StringIO()                 
    sys.stdout = capturedOutput                    
    compressing_strings("aa888n333dddd")                                  
    sys.stdout = sys.__stdout__                     

    assert capturedOutput.getvalue() == "(2, a) (3, 8) (1, n) (3, 3) (4, d)", f"Printed: {capturedOutput.getvalue()}, instead of (2, a) (3, 8) (1, n) (3, 3) (4, d)" 