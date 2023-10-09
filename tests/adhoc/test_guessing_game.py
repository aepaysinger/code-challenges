import io

import sys

from code_challenges.adhoc.guessing_game import GuessingGame


def test_guessing_game():
    guessing_game = GuessingGame("world", 3)
    guessing_game.guess("baby")

    assert guessing_game.guess_count == 1
    assert guessing_game.word_tracker == ["baby"]

    guessing_game.guess("earth")

    assert guessing_game.guess_count == 2
    assert guessing_game.word_tracker == ["baby", "earth"]


def test_guessing_game_print():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print(GuessingGame("world", 3))
    sys.stdout = sys.__stdout__

    assert (
        capturedOutput.getvalue()
        == "The guessing game! you have made 0 guesses and the words:[]\n"
    ), f"Printed: {capturedOutput.getvalue()}, instead of 'The guessing game! you have made 0 guesses and the words:[]\n'"


def test_guessing_game_win():
    guessing_game = GuessingGame("love", 2)

    assert guessing_game.guess("love") == "YOU WIN"


def test_guessing_game_wrong_word():
    guessing_game = GuessingGame("rainbow", 3)

    assert guessing_game.guess("color") == "you are wrong, 3 letter(s) are correct"


def test_guessing_game_all_guesses():
    guessing_game = GuessingGame("dog", 2)
    guessing_game.guess("cat")

    assert guessing_game.guess("wolf") == "game over"
