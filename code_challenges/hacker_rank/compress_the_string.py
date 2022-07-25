def compressing_strings(a_string):
    count = 0
    current_letter = a_string[0]
    compressed_string = []
    
    for letter in a_string:
        if letter == current_letter:
            count += 1
        else:
            compressed_string.append((count, current_letter))
            current_letter = letter
            count = 1
    return compressed_string
    # print(f'({count}, {current_letter})', end = '')
    

if __name__ == '__main__':
    # a_string = str(input())
    print(compressing_strings('1222311'))
# def compressing_strings(a_string):
#     count = 0
#     current_letter = a_string[0]

    
#     for letter in a_string:
#         if letter == current_letter:
#             count += 1
#         else:
#             print(f'({count}, {current_letter}) ', end = '')
#             current_letter = letter
#             count = 1
#     return f'({count}, {current_letter})', end = ''
#     print(f'({count}, {current_letter})', end = '')
    

# if __name__ == '__main__':
#     # a_string = str(input())
#     print(compressing_strings('1222311'))