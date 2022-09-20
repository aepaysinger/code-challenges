def scramble(s1, s2):
    matching_word = unscramble(s1, s2)
 
    return s2 == matching_word


def unscramble(s1, s2):
    matching_word = ""
    s1 = list(s1)
    for letter in s2:
        if letter in s1:
            matching_word += letter
            s1.remove(letter)
    return matching_word

if __name__ == "__main__":
    s1 = 'dmweyrrnbovczlge'
    s2 = 'dywegzwbvnm'
    print(scramble(s1, s2))