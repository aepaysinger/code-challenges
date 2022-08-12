def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    final_list = []
    for i in range(1, n + 1):
        final_list.append(i * x)
    return ", ".join(map(str, final_list))


if __name__ == "__main__":
    x = 2
    n = 5
    print(count_by(x, n))
