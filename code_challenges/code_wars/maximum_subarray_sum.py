def max_sequence(sequence):
    total = 0
    for number in sequence:
        if number > 0:
            total += 1
            break
    if total == 0:
        return total
    
    arrays_to_check = [(0, len(sequence)-1)]
    stop = len(sequence)-1
    
    
    j = 1
    
    for i in range(len(sequence)): 
        while sequence[j] >= 0 and j != stop:
            j += 1
        if j == stop:
            arrays_to_check.append((i,j))
        else:
            arrays_to_check.append((i, j-1))

        
        print(arrays_to_check)
        print(sequence[i], sequence[j])

    for arrays in arrays_to_check:
        if sum(sequence[arrays[0]:arrays[1]]) > total:
            total = sum(sequence[arrays[0]:arrays[1]])
        
     
            
        
    # for start_stop in arrays_to_check:
    #     if start_stop[1] == len(sequence) - 1:
    #         if sum(sequence[start_stop[0]:start_stop[1]]) > total:
    #             total = sum(sequence[start_stop[0]:start_stop[1]])
    #     if sum(sequence[start_stop[0]:start_stop[1]+1]) > total:
    #         total = sum(sequence[start_stop[0]:start_stop[1]+1])
    return total, arrays_to_check
dont move i until j has gone to the end of the list

if __name__ == "__main__":
    sequence = [-2, 1, -3, 4, -1, 2, 1, -5, 4] #(0,8) (0,2) (4,6) 
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