def get_polymers():
    with open("code_challenges/advent_of_code/polymers_input") as polymers_input:
        polymers = polymers_input.read()

    return list(polymers)


def find_polymers_with_no_reactions(polymers):
    
    # print(polymers)
    while True:
        edited_polymers = []
        i = 0
        j = 1
        for polymer in polymers:
            if i == len(polymers) - 1:
                edited_polymers.append(polymers[i])
                break       
            if check_two_letters(polymers[i], polymers[j]):
                i += 2
                j += 2
            else:
                edited_polymers.append(polymers[i])
                i += 1
                j += 1
 
        if polymers == edited_polymers:
            break
        polymers = edited_polymers

    return polymers 

def check_two_letters(letter_one, letter_two):
    if (letter_one.islower() and letter_two.isupper()) and (letter_two.lower() == letter_one):
        return True
    elif (letter_one.isupper() and letter_two.islower()) and (letter_two.upper() == letter_one):
        return True
    else:
        return False
    

def find_polymer_characters():
    polymers = get_polymers()
    polymer_counts = {}
    for character in polymers:
        polymer_counts[f"{character.upper()}/{character.lower()}"] = polymer_counts.get(f"{character.upper()}/{character.lower()}", 0)
    return polymer_counts


def find_polymer_counts():
    polymers = get_polymers()
    print(polymers)
    
    polymer_count = find_polymer_characters()
    print(polymer_count)
    for big,_,little in polymer_count.keys():
        edited_polymers = []
        for character in polymers:
            if character == big:
                continue
            elif character == little:
                continue
            else:
                edited_polymers.append(character)
        edited_polymers = find_polymers_with_no_reactions(edited_polymers)
        polymer_count[big,_,little] = len(edited_polymers)
        polymers = get_polymers()
        
        # edited_polymers = find_polymers_with_no_reactions(polymers)
        # polymer_count[big,_,little] = len(edited_polymers)
        
    print(polymer_count)

            



# print(get_polymers())
# print(find_polymers_with_no_reactions(get_polymers()))
# print(find_polymer_characters())
print(find_polymer_counts())
