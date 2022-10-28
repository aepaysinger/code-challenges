def max_sequence(sequence):
    total = 0
    for number in sequence:
        if number > 0:
            total += 1
            break
    if total == 0:
        return total
    
    arrays_to_check = []
    j = len(sequence) - 1
    i = 0
    
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
        j -= 1
        i += 1
    for start_stop in arrays_to_check:
        if start_stop[1] == len(sequence) - 1:
            if sum(sequence[start_stop[0]:start_stop[1]]) > total:
                total = sum(sequence[start_stop[0]:start_stop[1]])
        if sum(sequence[start_stop[0]:start_stop[1]+1]) > total:
            total = sum(sequence[start_stop[0]:start_stop[1]+1])
    return total


if __name__ == "__main__":
    sequence = [-2, 1, -3, 4, -1, 2, 1, -5, 4] #(1,8) (3,6) 
    print(max_sequence(sequence))
    # i start or after neg
    # j last item or before neg
# def max_sequence(sequence):
#     total = 0
#     for number in sequence:
#         if number > 0:
#             total += 1
#             break
#     if total == 0:
#         return total
    
    
#     for i in range(len(sequence)):
#         j = len(sequence)
#         if sequence[i] < 1:
#             continue
#         while j > i:
#             if sequence[j-1] > 0 and sum(sequence[i:j]) > total:
#                 total = sum(sequence[i:j])
#             j -= 1
#     return total