# word guessing game(class)
# play or guess method - you put in a guess
# it will tell you if the guess is right or wrong, will tell you how many letters are correct in your guess
# certain amount of guesses b4 game over
# cant guess the same word twice
# we give the word and the amount of times they can guess
class GuessingGame:
    def __init__(self, word, guesses):
        self.word = word
        self.guesses = guesses
        self.guess_count = 0
        self.word_tracker = []

    def guess(self, guess_word):
        matching_letters = 0
        self.guess_count += 1
        self.word_tracker.append(guess_word)

        if guess_word == self.word:
            return "YOU WIN"
        else:
            for letter in guess_word:
                if letter in self.word:
                    matching_letters += 1
            if self.guesses == self.guess_count:
                return "game over"
            else:
                return f"you are wrong, {matching_letters} letter(s) are correct"

    def __repr__(self):
        return f"The guessing game! you have made {self.guess_count} guesses and the words:{self.word_tracker}"


if __name__ == "__main__":
    gg = GuessingGame("love", 2)
    gg.guess("love")
