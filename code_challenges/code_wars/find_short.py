def find_short(s):
    shortest = ""
    seperated_words = s.split(" ")

    for word in seperated_words:
        if shortest == "":
            shortest += word
        if len(word) < len(shortest):
            shortest = word
    return len(shortest)


if __name__ == "__main__":
    s = "bitcoin take over the world maybe who knows perhaps"
    print(find_short(s))
