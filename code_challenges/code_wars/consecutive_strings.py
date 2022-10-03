def consecutive_strings(names, k):
    if k > len(names):
        return ""
    length = 0
    concatenated_string = ""
    for i in range(0, k, 1):
        word_groups = names[i : i + k]
        words = "".join(word_groups)
        if len(words) > length:
            length = len(words)
            concatenated_string = words

    return concatenated_string


if __name__ == "__main__":
    names = ["zone", "theta", "abigail", "form", "libe", "zas"]
    k = 2
    print(consecutive_strings(names, k))
