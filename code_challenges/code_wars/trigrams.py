def trigrams(phrase):
    i = 0
    j = 3
    trigrams = []
    updated_phrase = phrase.replace(" ", "_")
    while i < len(phrase):
        for character in updated_phrase:
            print(i, j, updated_phrase[i:j])
            trigrams.append(updated_phrase[i:j])
            i += 1
            j += 1

    return " ".join(trigrams[:-2])


if __name__ == "__main__":
    phrase = "divided by 3"
    print(trigrams(phrase))
