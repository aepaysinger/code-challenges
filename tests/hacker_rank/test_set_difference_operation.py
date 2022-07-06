import io
import sys

from code_challenges.hacker_rank.set_difference_operation import learning_difference


def test_learning_difference_a():
    roll_numbers_english = input().split(' ')       #set up for the function
    roll_numbers_french = input().split(' ')
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    learning_difference()                                  # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.

    assert capturedOutput.getvalue() == "Not Weird\n", f"Printed: {capturedOutput.getvalue()}, instead of Not Weird"