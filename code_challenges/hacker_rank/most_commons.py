def make_logo(name):
    letters = {}
    for letter in name:
        try:
            letters[letter] += 1
        except KeyError:
            letters[letter] = 1

    top1 = ("",0)
    top2 = ("",0)
    top3 = ("",0)
    for letter in sorted(letters):
        if letters[letter] > top1[1]:
            top3 = top2
            top2 = top1
            top1 = (letter, letters[letter])
        elif letters[letter] >top2[1]:
            top3 = top2
            top2 = (letter, letters[letter])
        elif letters[letter] > top3[1]:
            top3 = (letter, letters[letter])

    return f"{' '.join(map(str, top1))}\n{' '.join(map(str, top2))}\n{' '.join(map(str, top3))}"


if __name__ == '__main__':
    s = "aabbbccde"
    print(make_logo(s))





# if __name__ == "__main__":
#     company_name = "aabbbccde"
#     print(make_company_logo(company_name))

    # def make_company_logo(company_name):
    # # finding counts for each letter
    # seperate_letters = {}
    # for letter in company_name:
    #     if letter not in seperate_letters:
    #         seperate_letters[letter] = 1
    #     else:
    #         seperate_letters[letter] += 1
    # # find the top 3 used letters
    # first = 0
    # second = 0
    # third = 0
    # for letters in seperate_letters:
    #     if seperate_letters[letters] > first:
    #         third = second
    #         second = first
    #         first = seperate_letters[letters]
            
            
            

    # print(seperate_letters)
    # print(first, second, third)