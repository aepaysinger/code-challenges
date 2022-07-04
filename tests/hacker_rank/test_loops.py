import io
import sys

from code_challenges.hacker_rank.loops import fun_stuff



def test_fun_stuff():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    fun_stuff(4)                                  # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.

    assert capturedOutput.getvalue() == "".join([f"{i*i}\n" for i in range(4)]), f"Printed: {capturedOutput.getvalue()}, instead of {"".join(["(i*i)\n" for i in range(4)])}"
