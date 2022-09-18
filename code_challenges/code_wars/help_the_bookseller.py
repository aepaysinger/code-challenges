def help_the_bookseller(codes, categories):
    category_with_amount = category_amount(codes)
    
    final_result = ""
    for letter in categories:
        if letter in category_with_amount:
            final_result += f"({letter} : {category_with_amount[letter]}) - "
        else:
            final_result += f"({letter} : 0) - "
    
        
    return final_result[:-3]
    

def category_amount(codes):
    category_with_amount = {}
    for code in codes:
        new_code = code.split()
        if new_code[0][0] in category_with_amount:
            category_with_amount[new_code[0][0]] += int(new_code[1])
        else:
            category_with_amount[new_code[0][0]] = int(new_code[1])
    return category_with_amount
    
        
    


if __name__ == "__main__":
    codes = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
    categories = ["E", "F", "G", "H"]
    print(help_the_bookseller(codes, categories))
    

   