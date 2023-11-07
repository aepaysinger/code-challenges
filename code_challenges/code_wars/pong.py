class Pong:
    def __init__(self, max_score):
        self.max_score = max_score
        self.score = {"1": 0, "2": 0}
        self.player = "2"

    def play(self, ball_pos, player_pos):
        if self.player == "1":
            self.player = "2"
        else:
            self.player = "1"

        if self.score["1"] == self.max_score:
            self.score["1"] += 1
            return "Player 1 has won the game!"
        elif self.score["2"] == self.max_score:
            self.score["2"] += 1
            return "Player 2 has won the game!"
        elif self.score["1"] > self.max_score or self.score["2"] > self.max_score:
            return "Game Over!"
        elif ball_pos <= player_pos + 3 and ball_pos >= player_pos - 3:
            self.score[self.player] += 1
            return f"Player {self.player} has hit the ball!"
        else:
            return f"Player {self.player} has missed the ball!"
