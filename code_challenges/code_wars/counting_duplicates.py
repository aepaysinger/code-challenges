def counting_duplicates(s):
    counter = 0
    tracker = {}
    s = s.upper()
    for character in s:
        if character in tracker:
            tracker[character] += 1
        else:
            tracker[character] = 1
    for key in tracker:
        if tracker[key] > 1:
            counter += 1
    return counter


if __name__ == "__main__":
    s = "Unbhs7gvjKJhbaNhj"
    print(counting_duplicates(s))
