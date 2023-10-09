def max_sequence(sequence):
    arrays_to_check = []
    j = len(sequence) - 1
    i = 0
    if sequence == []:
        return 0
    for _ in range(len(sequence)):
        while sequence[i] < 1:
            i += 1
        while sequence[j] < 1:
            j -= 1
        if i >= j:
            break
        start = i
        stop = j
        arrays_to_check.append((start, stop))
        i += 1
        j -= 1
    return max(arrays_to_check[1])
if __name__ == "__main__":
    sequence = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
    print(max_sequence(sequence))
