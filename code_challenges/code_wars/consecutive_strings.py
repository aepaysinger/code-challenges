def consecutive_strings(names, k):
    if k > len(names) or k <= 0:
        return ""
    length = 0
    concatenated_string = ""
    for i in range(len(names) - k + 1):
        word_groups = names[i : i + k]
        print(i, word_groups)
        words = "".join(word_groups)
        if len(words) > length:
            length = len(words)
            concatenated_string = words

    return concatenated_string


if __name__ == "__main__":
    names = ["zone", "abigail", "theta", "form", "libe", "zas"]
    k = 3
    print(consecutive_strings(names, k))
