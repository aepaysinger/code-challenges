def merge_the_tools(string, k):
    sub_strings = []
    for _ in range(k):
        sub_strings.append(string[0:3])
        string = string[3:]
    final_strings = []
    for sub_string in sub_strings:
        for _ in range(k-1):
            if sub_string[0] == sub_string[1]:
                sub_string = sub_string[1:]
            else:
                final_strings.append(sub_string[0:2])
                sub_string = sub_string[1:]
    
    for i in range(k):
        print(final_strings[i])

    # print(sub_strings, final_strings)


if __name__ == '__main__':
    # string, k = input(), int(input())
    merge_the_tools("AABCAAADA", 3)