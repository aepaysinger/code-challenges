def consecutive_strings(starr, k):
    length = 0
    concatenated_string = ""
    for word in range(0, len(starr), 1):
        word_groups = starr[word : word + k]
        if len(word_groups) == k:
            words = "".join(word_groups)
            if len(words) > length:
                length = len(words)
                concatenated_string = words

    return concatenated_string


if __name__ == "__main__":
    starr = ["zone", "theta", "abigail", "form", "libe", "zas"]
    k = 2
    print(consecutive_strings(starr, k))
