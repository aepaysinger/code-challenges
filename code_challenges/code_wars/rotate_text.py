def rotate(str_):
    rotated_words = []

    for _ in range(len(str_)):
        rotated_words.append(str_[1:] + str_[0])
        str_ = str_[1:] + str_[0]
    return rotated_words
