import io
import sys

from code_challenges.hacker_rank.arithmetic_operators import some_stuff


def test_some_stuff_a():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    some_stuff(7, 3)                                  # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.

    assert capturedOutput.getvalue() == "10\n4\n21\n", f"Printed: {capturedOutput.getvalue()}, instead of 10\n4\n21"

def test_some_stuff_b():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    some_stuff(-6, 2)                                  # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.

    assert capturedOutput.getvalue() == "-4\n-8\n-12\n", f"Printed: {capturedOutput.getvalue()}, instead of -4\n-8\n-12"

def test_some_stuff_c():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    some_stuff(5, 9)                                  # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.

    assert capturedOutput.getvalue() == "14\n-4\n45\n", f"Printed: {capturedOutput.getvalue()}, instead of 14\n-4\n45"
