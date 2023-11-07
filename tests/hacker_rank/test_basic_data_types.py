import io
import sys

from code_challenges.hacker_rank.basic_data_types import basic_data_types


def test_basic_data_types_a():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    basic_data_types(
        [
            ["insert", "0", "5"],
            ["insert", "1", "10"],
            ["insert", "0", "6"],
            ["print"],
            ["remove", "6"],
            ["append", "9"],
            ["append", "1"],
            ["sort"],
            ["print"],
            ["pop"],
            ["reverse"],
            ["print"],
        ]
    )
    sys.stdout = sys.__stdout__

    assert (
        capturedOutput.getvalue() == "[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]\n"
    ), f"Printed: {capturedOutput.getvalue()}, instead of [6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]"
