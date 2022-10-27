def max_sequence(sequence):
    total = 0
    for number in sequence:
        if number > 0:
            total += 1
    if total == 0:
        return total
    else:
        for i, number in enumerate(sequence):
            j = len(sequence)
            while j > i:
                if sequence[j-1] > 0:
                    if sum(sequence[i:j]) > total:
                        total = sum(sequence[i:j])
                        j -= 1 
                    else:
                        j -= 1
                else:
                    j -= 1        
                   
    return total

        

        






    
    

if __name__ == "__main__":
    sequence = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]
    print(max_sequence(sequence))