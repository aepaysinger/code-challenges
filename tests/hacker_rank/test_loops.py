import io
import sys

from code_challenges.hacker_rank.loops import fun_stuff


def test_fun_stuff_a():
    reps = 4
    expected = "".join([f"{i*i}\n" for i in range(reps)])
    capturedOutput = io.StringIO()                  
    sys.stdout = capturedOutput                     
    fun_stuff(reps)                                  
    sys.stdout = sys.__stdout__                     

    assert capturedOutput.getvalue() == expected, f"Printed: {capturedOutput.getvalue()}, instead of {expected}"


def test_fun_stuff_b():
    reps = -3
    expected = "".join([f"{i*i}\n" for i in range(reps)])
    capturedOutput = io.StringIO()                  
    sys.stdout = capturedOutput                     
    fun_stuff(reps)                                  
    sys.stdout = sys.__stdout__                     

    assert capturedOutput.getvalue() == expected, f"Printed: {capturedOutput.getvalue()}, instead of {expected}"


def test_fun_stuff_c():
    reps = 7
    expected = "".join([f"{i*i}\n" for i in range(reps)])
    capturedOutput = io.StringIO()                  
    sys.stdout = capturedOutput                     
    fun_stuff(reps)                                  
    sys.stdout = sys.__stdout__                     

    assert capturedOutput.getvalue() == expected, f"Printed: {capturedOutput.getvalue()}, instead of {expected}"

