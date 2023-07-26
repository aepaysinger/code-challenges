def arrange(s):
    t = []
    length = len(s)

    for i in range((len(s) // 2) + 1):
        if i % 2 == 0:
            t.append(s[i])
            t.append(s[-1 - i])
        else:
            t.append(s[-1 - i])
            t.append(s[i])
    del t[length:]
    return t


if __name__ == "__main__":
    s = [1, 2, 3, 4, 5]
    print(arrange(s))
