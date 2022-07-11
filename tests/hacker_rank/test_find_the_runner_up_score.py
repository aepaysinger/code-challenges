import io
import sys

from code_challenges.hacker_rank.find_the_runner_up_score import runner_up


def test_runner_up_low_first():
    capturedOutput = io.StringIO()                 
    sys.stdout = capturedOutput                     
    runner_up([2, 3, 6, 6, 5])                                 
    sys.stdout = sys.__stdout__                    

    assert capturedOutput.getvalue() == "5\n", f"Printed: {capturedOutput.getvalue()}, instead of 5"


def test_runner_up_tie():
    capturedOutput = io.StringIO()                 
    sys.stdout = capturedOutput                     
    runner_up([8, 8, 8, 8])                                 
    sys.stdout = sys.__stdout__                    

    assert capturedOutput.getvalue() == "it's a tie!\n", f"Printed: {capturedOutput.getvalue()}, instead of it's a tie"


def test_runner_up_high_first():
    capturedOutput = io.StringIO()                 
    sys.stdout = capturedOutput                     
    runner_up([7, 6, 3, 3, 5])                                 
    sys.stdout = sys.__stdout__                    

    assert capturedOutput.getvalue() == "6\n", f"Printed: {capturedOutput.getvalue()}, instead of 6"
    