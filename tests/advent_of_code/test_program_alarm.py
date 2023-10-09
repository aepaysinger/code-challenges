import pytest

from unittest.mock import patch


from code_challenges.advent_of_code.program_alarm import (
    final_result,
    get_next_noun_verb_pair,
    opcode_instructions,
)


@patch("code_challenges.advent_of_code.program_alarm.opcode_integers")
def test_opcode_instructions(opcode_integers_mock):
    opcode_integers_mock.return_value = [1, 3, 2, 1, 2, 4, 1, 0, 99, 6, 7]
    actual = opcode_instructions(4)
    expected = 0, 0

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.program_alarm.opcode_instructions")
def test_final_result(opcode_instructions_mock):
    opcode_instructions_mock.return_value = 9, 12
    actual = final_result()
    expected = 912

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_get_next_noun_verb_pair():
    pairs = get_next_noun_verb_pair()
    next(pairs)
    next(pairs)
    next(pairs)

    assert next(pairs) == (0, 3)


def test_get_next_noun_verb_pair_stop_itteration():
    pairs = get_next_noun_verb_pair()

    for _ in range(9999):
        next(pairs)
    next(pairs)

    with pytest.raises(RuntimeError) as exc_info:
        next(pairs)
    assert exc_info.value.args[0] == "generator raised StopIteration"


def test_opcode_instructions_stop_itteration():
    with pytest.raises(RuntimeError) as exc_info:
        opcode_instructions(4)
    assert exc_info.value.args[0] == "generator raised StopIteration"
