def make_logo(name):
    letters = {}
    for letter in name:
        if letter == " ":
            letters[letter] = 0
            continue
        try:
            letters[letter] += 1
        except KeyError:
            letters[letter] = 1

    top1 = ("", 0)
    top2 = ("", 0)
    top3 = ("", 0)
    for letter in sorted(letters):
        if letters[letter] > top1[1]:
            top3 = top2
            top2 = top1
            top1 = (letter, letters[letter])
        elif letters[letter] > top2[1]:
            top3 = top2
            top2 = (letter, letters[letter])
        elif letters[letter] > top3[1]:
            top3 = (letter, letters[letter])

    return f"{' '.join(map(str, top1))}\n{' '.join(map(str, top2))}\n{' '.join(map(str, top3))}"


if __name__ == "__main__":
    name = "crazy company name"
    print(make_logo(name))
