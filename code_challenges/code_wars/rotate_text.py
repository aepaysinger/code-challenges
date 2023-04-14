def rotate(str_):
    rotated_words = []
    word = str_
    for _ in range(len(str_)):
        rotated_words.append(word[1:] + word[0])
        word = word[1:] + word[0]
    return rotated_words
