def highest_scoring_word(words):
    letter_points = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }
    words_list = words.split()
    score_board = {}
    for word in words_list:
        word_points = 0
        for letter in word:
            word_points += letter_points[letter]
        score_board[word] = word_points
    highest_word = None
    highest_score = 0
    for word in score_board:
        if score_board[word] > highest_score:
            highest_score = score_board[word]
            highest_word = word
        elif score_board[word] == highest_score:
            highest_word += " " + word

    return highest_word


if __name__ == "__main__":
    words = "not sure what other test to run"
    print(highest_scoring_word(words))
