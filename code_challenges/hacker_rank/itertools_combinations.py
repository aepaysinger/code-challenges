from itertools import combinations


def making_combinations(a_string, a_number):
    list_a_string = list(a_string)
    list_a_string = sorted(list_a_string, key=str.lower) 
    final_combinations = []
    for count in range(1, a_number + 1):
        combinations_with_count = list(combinations(list_a_string, count))
        for groups in combinations_with_count:
            final_combinations.append("".join(groups))
    return "\n".join(final_combinations)


if __name__ == '__main__':
    print(making_combinations('ABCD', 3))

      # CREATE A STRING THAT IS EXACTLY WHAT I WANT TO PRINT OUT, THEN IN THE IF __NAME__ == '__MAIN__' PRINT THE FUNCTION        
    # for number in range(1,a_number + 1):
    #     print(number)
