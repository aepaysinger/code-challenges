from code_challenges.code_wars.pong import Pong


def test_pong():
    game = Pong(2)

    assert game.play(55, 53) == "Player 1 has hit the ball!"
    assert game.play(100, 97) == "Player 2 has hit the ball!"
    assert game.play(0, 4) == "Player 1 has missed the ball!"
    assert game.play(25, 25) == "Player 2 has hit the ball!"
    assert game.play(75, 25) == "Player 2 has won the game!"
    assert game.play(50, 50) == "Game Over!"


def test_pon2():
    game = Pong(2)

    assert game.play(0, 2) == "Player 1 has hit the ball!"
    assert game.play(60, 65) == "Player 2 has missed the ball!"
    assert game.play(40, 41) == "Player 1 has hit the ball!"
    assert game.play(100, 103) == "Player 1 has won the game!"
    assert game.play(37, 45) == "Game Over!"
