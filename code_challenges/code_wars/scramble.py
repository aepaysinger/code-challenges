def scramble(s1, s2):
    counter1, counter2 = count_characters(s1, s2)
    for character in counter2:
        if character not in counter1:
            return False
        if counter2[character] > counter1[character]:
            return False
        
    return True
def count_characters(s1,s2):
    s1_amount = {}
    s2_amount = {}
    for character in s1:
        if character in s1_amount:
            s1_amount[character] += 1
        else:
            s1_amount[character] = 1 
    for character in s2:
        if character in s2_amount:
            s2_amount[character] += 1
        else:
            s2_amount[character] = 1
    print(s1_amount, s2_amount) 
    return s1_amount, s2_amount
if __name__ == "__main__":
    s1 = "ss"
    s2 = "sa"
    print(scramble(s1, s2))

#     def scramble(s1, s2):
#     matching_word = unscramble(s1, s2)
 
#     return s2 == matching_word


# def unscramble(s1, s2):
#     matching_word = ""
#     s1 = list(s1)
#     for letter in s2:
#         if letter in s1:
#             matching_word += letter
#             s1.remove(letter)
#     return matching_word