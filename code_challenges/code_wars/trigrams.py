def trigrams(phrase):
    char_per_trigram = 3
    trigrams = []

    updated_phrase = phrase.replace(" ", "_")

    for i in range(len(updated_phrase) - char_per_trigram + 1):

        trigrams.append(updated_phrase[i : i + char_per_trigram])

    return " ".join(trigrams)


if __name__ == "__main__":
    phrase = "divided by 3"  
    print(trigrams(phrase))
