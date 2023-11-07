def cut_rope(length, m, n):
    rope = ["-" for _ in range(length)]
    different_lengths = {}
    rope_with_cuts = []
    count_m = 0
    count_n = 0
    for i, section in enumerate(rope):
        rope_with_cuts.append(("-"))
        count_m += 1
        count_n += 1
        if count_m == m:
            rope_with_cuts.append(".")
            count_m = 0
        if count_n == n:
            if (i + 1) % m == 0 and (i + 1) % n == 0:
                count_n = 0
            else:
                rope_with_cuts.append(".")
                count_n = 0

    length_count = 0

    for i in range(len(rope_with_cuts)):
        if i == (len(rope_with_cuts) - 1) and rope_with_cuts[i] == "-":
            length_count += 1
            different_lengths[str(length_count) + "cm"] = (
                different_lengths.get(str(length_count) + "cm", 0) + 1
            )
        elif rope_with_cuts[i] == "-":
            length_count += 1
        elif rope_with_cuts[i] == "." and length_count == 0:
            continue
        elif rope_with_cuts[i] == ".":
            different_lengths[str(length_count) + "cm"] = (
                different_lengths.get(str(length_count) + "cm", 0) + 1
            )
            length_count = 0

    rope_length = list(different_lengths.keys())
    rope_length.sort()
    sorted_rope_lengths = {i: different_lengths[i] for i in rope_length}
    return sorted_rope_lengths


if __name__ == "__main__":
    length = 10
    m = 2
    n = 3
    print(cut_rope(length, m, n))
