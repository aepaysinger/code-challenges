import io
import sys

from code_challenges.hacker_rank.set_difference_operation import learning_difference


def test_weird_stuff_not_weird_a():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    weird_stuff(4)                                  # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.

    assert capturedOutput.getvalue() == "Not Weird\n", f"Printed: {capturedOutput.getvalue()}, instead of Not Weird"