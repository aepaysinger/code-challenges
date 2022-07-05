import io
import sys

from code_challenges.hacker_rank.division import fun_division


def test_fun_division_a():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    fun_division(7, 2)                                  # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.

    assert capturedOutput.getvalue() == "3\n3.5\n", f"Printed: {capturedOutput.getvalue()}, 3\n3.5"

def test_fun_division_b():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    fun_division(-3, 8)                                  # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.

    assert capturedOutput.getvalue() == "-1\n-0.38\n", f"Printed: {capturedOutput.getvalue()}, -1\n-0.38"

def test_fun_division_c():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    fun_division(4, 9)                                  # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.

    assert capturedOutput.getvalue() == "0\n0.44\n", f"Printed: {capturedOutput.getvalue()}, 0\n0.44"   

def test_fun_division_d():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    fun_division(16, 4)                                  # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.

    assert capturedOutput.getvalue() == "4\n4.0\n", f"Printed: {capturedOutput.getvalue()}, 4\n4.0"  