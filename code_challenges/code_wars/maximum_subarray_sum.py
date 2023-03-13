def max_sequence(sequence):

    total = 0

    for i in range(len(sequence)):
        j = len(sequence)
        if sequence[i] < 1:
            continue
        while j > i:
            if sequence[j-1] > 0 and sum(sequence[i:j]) > total:
                total = sum(sequence[i:j])
            j -= 1
    return total

if __name__ == "__main__":
    sequence = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
    print(max_sequence(sequence))
