def make_company_logo(company_name):
    # finding counts for each letter
    seperate_letters = {}
    for letter in company_name:
        if letter not in seperate_letters:
            seperate_letters[letter] = 1
        else:
            seperate_letters[letter] += 1
    # find the top 3 used letters
    first = 0
    second = 0
    third = 0
    for letters in seperate_letters:
        if seperate_letters[letters] > first:
            third = second
            second = first
            first = seperate_letters[letters]
            
            
            

    print(seperate_letters)
    print(first, second, third)





if __name__ == "__main__":
    company_name = "aabbbccde"
    make_company_logo(company_name)