import io
import sys

from code_challenges.hacker_rank.intergers_come_in_all_sizes import big_intergers


def test_big_intergers_odd():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    big_intergers(9, 29, 7, 27)
    sys.stdout = sys.__stdout__

    assert (
        capturedOutput.getvalue() == "4710194409608608369201743232\n"
    ), f"Printed: {capturedOutput.getvalue()}, instead of 4710194409608608369201743232"


def test_big_intergers_even():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    big_intergers(8, 44, 2, 50)
    sys.stdout = sys.__stdout__

    assert (
        capturedOutput.getvalue() == "5444517870735015415413994844808198225920\n"
    ), f"Printed: {capturedOutput.getvalue()}, instead of 5444517870735015415413994844808198225920"


def test_big_intergers_negative():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    big_intergers(-3, 24, 7, 33)
    sys.stdout = sys.__stdout__

    assert (
        capturedOutput.getvalue() == "7730993719707444806566630888\n"
    ), f"Printed: {capturedOutput.getvalue()}, instead of 7730993719707444806566630888"
