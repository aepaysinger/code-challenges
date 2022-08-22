def find_short(s):
    seperated_words = s.split(" ")
    shortest = seperated_words[0]

    for word in seperated_words:
        if len(word) < len(shortest):
            shortest = word
    return len(shortest)


if __name__ == "__main__":
    s = "bitcoin take over the world maybe who knows perhaps"
    print(find_short(s))
