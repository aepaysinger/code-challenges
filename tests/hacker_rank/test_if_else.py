import io
import sys

from code_challenges.hacker_rank.if_else import weird_stuff


def test_weird_stuff_not_weird_a():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    weird_stuff(4)                                  # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.

    assert capturedOutput.getvalue() == "Not Weird\n", f"Printed: {capturedOutput.getvalue()}, instead of Not Weird"
# not the \n in the string

def test_weird_stuff_weird_a():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    weird_stuff(3)                                  # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.

    assert capturedOutput.getvalue() == "Weird\n", f"Printed: {capturedOutput.getvalue()}, instead of Weird"

def test_weird_stuff_weird_b():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    weird_stuff(8)                                  # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.

    assert capturedOutput.getvalue() == "Weird\n", f"Printed: {capturedOutput.getvalue()}, instead of Weird"

def test_weird_stuff_not_weird_b():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    weird_stuff(22)                                  # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.

    assert capturedOutput.getvalue() == "Not Weird\n", f"Printed: {capturedOutput.getvalue()}, instead of Not Weird"






