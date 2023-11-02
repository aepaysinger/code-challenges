def pattern(n):
    if n <= 0:
        return ""
    magic_n = str(n)[-1]
    the_pattern = [[magic_n for i in range(n)]]

    num = int(magic_n) - 1

    for i in range(1, n):
        new_pattern = []
        old_pattern = the_pattern[i - 1]
        for _ in range(i):
            new_pattern.append(old_pattern[_])
        for _ in range(n - i):
            new_pattern.append(str(num))
        if num == 0:
            num = 9
        else:
            num -= 1

        the_pattern.append(new_pattern)

    the_pattern = ["".join(pattern) for pattern in the_pattern]
    the_pattern = "\n".join(the_pattern)
    return the_pattern
