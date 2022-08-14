def split_the_string(s):
    list_of_pairs = []
    pairs = ""
    for letter in s:
        pairs += letter
        if len(pairs) == 2:
            list_of_pairs.append(pairs)
            pairs = ""
    if len(s) % 2 != 0:
        pairs = s[-1] + "_"
        list_of_pairs.append(pairs)

    return list_of_pairs


if __name__ == "__main__":
    s = "abcdefg"
    print(split_the_string(s))
