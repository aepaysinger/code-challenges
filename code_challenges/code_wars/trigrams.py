def trigrams(phrase):
    i = 0
    j = 2
    
    while i < len(phrase):
        trigrams = [phrase[i:j], for character in phrase]
        i += 1
        j +=1
    print(trigrams)



if __name__ == "__main__":
    phrase = "the quick red"
    print(trigrams(phrase)