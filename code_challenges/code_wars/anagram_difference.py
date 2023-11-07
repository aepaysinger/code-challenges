def anagram_difference(w1, w2):
    w1_count = {}
    w2_count = {}
    characters_in_both_words = []
    for character in w1:
        w1_count[character] = w1_count.get(character, 0) + 1
    for character in w2:
        w2_count[character] = w2_count.get(character, 0) + 1

    for character, count in w1_count.items():
        if character in w2_count:
            if count > w2_count[character]:
                for i in range(w2_count[character]):
                    characters_in_both_words.append(character)
            else:
                for i in range(count):
                    characters_in_both_words.append(character)

    return (len(w1) - len(characters_in_both_words)) + (
        len(w2) - len(characters_in_both_words)
    )
