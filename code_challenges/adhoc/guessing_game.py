#word guessing game(class)
# play or guess method - you put in a guess
# it will tell you if the guess is right or wrong, will tell you how many letters are correct in your guess
# certain amount of guesses b4 game over
# cant guess the same word twice
# we give the word and the amount of times they can guess
class GuessingGame:
    def __init__(self, guesses, word):
        self.guesses = guesses
        self.word = word
        

    def guess(self, guess_word):
        if guess_word == word:
            print("YOU WIN")
        




if __name__ == "__main__":
    # word = "world"
    guesses = 2
    guess_word = "world"
    guessing_game = GuessingGame(guesses, "world")
    guessing_game.guess(guess_word)
    
    