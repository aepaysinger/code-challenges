def max_sequence(sequence):
    total = sum(sequence)
    for number in sequence:
        if number > 0:
            total += 1
    if total == 0:
        return total
    else:
        i = 0
        j = 1
        while j <= len(sequence):
            old_sequence = sum(sequence[i:j])
            new_sequence = sum(sequence[i:j+1])
            if old_sequence < new_sequence:
                old_sequence = new_sequence
                j += 1
            else:
                i = j
                j = i + 1

        
        






    
    return new_sequence

if __name__ == "__main__":
    sequence = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]
    print(max_sequence(sequence))