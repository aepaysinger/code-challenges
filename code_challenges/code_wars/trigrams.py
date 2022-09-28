def trigrams(phrase):
    i = 0
    j = 3
    trigrams = []
    updated_phrase = phrase.replace(" ", "_")
    while i < len(phrase):
        for character in updated_phrase:
            
            trigrams.append(updated_phrase[i:j])
            i += 1
            j += 1

    return " ".join([trigram for trigram in trigrams if len(trigram) == 3])

if __name__ == "__main__":
    phrase = "the quick red"
    print(trigrams(phrase))