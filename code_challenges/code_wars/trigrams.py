def trigrams(phrase):
    j = 3
    trigrams = []

    updated_phrase = phrase.replace(" ", "_")
    
    for i in range(len(updated_phrase)):
        if len(updated_phrase[i:j]) == 3:
            trigrams.append(updated_phrase[i:j])
            j += 1
        else:
            return " ".join(trigrams)


if __name__ == "__main__":
    phrase = "divided by 3"
    print(trigrams(phrase))
