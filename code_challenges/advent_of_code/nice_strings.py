def get_text_to_check():
    with open("./code_challenges/advent_of_code/file_of_strings") as input:
        text_to_check = input.read().split("\n")
    return text_to_check


def find_vowels(text):
    vowels = ("a", "e", "i", "o", "u")
    count = 0

    for character in text:
        if character in vowels:
            count += 1
    if count >= 3:
        return True
    return False


def find_double_letter(text):
    j = 1
    for i, character in enumerate(text):
        if j == len(text):
            return False
        elif text[i] == text[j]:
            return True
        j += 1


def find_subtext(text):
    pairs = ("ab", "cd", "pq", "xy")
    j = 1
    for pair in pairs:
        if pair in text:
            return False
    return True


def find_double_pair(text):
    pairs = set()

    for i in range(len(text)- 1):
        if (text[i:i+2] in pairs) and (text[i:i+2] != text[i-1:i+1]):
            return True

        pairs.add(text[i:i+2])
    
    return False


def find_the_pattern(text):
    for i in range(len(text) - 2):
        if text[i] == text[i + 2]:
            return True
    return False


def find_nice_string():
    count = 0
    for text in get_text_to_check():
        if find_vowels(text) and find_double_letter(text) and find_subtext(text):
            count += 1
    return count


def find_nice_string_2():
    count = 0
    for text in get_text_to_check():
        if find_double_pair(text) and find_the_pattern(text):
            count += 1
    return count


# print(get_text_to_check())
# print(find_vowels("ugknbfddgicrmopn"))
# print(find_double_letter("ugknbfdgicrmopn"))
# print(find_subtext("ugknbfddgicrmopn"))
# print(find_nice_string())
# print(find_double_pair("qljhvhtzxxxzqqjkmpb"))
# print(find_the_pattern("qjhvhtzxzqqjkmpb"))
print(find_nice_string_2())  # 65 wrong, and 67, 69, 50, 101
# print(find_double_pair("9jhvhtzxzqqjkmpb"))
