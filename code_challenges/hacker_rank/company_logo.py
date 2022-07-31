def make_logo(name):
    letters = {}
    for letter in name:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    top1 = ["",0]
    top2 = ["",0]
    top3 = ["",0]
    for letter in letters:
        if letters[letter] > top1[1]:
            top3 = top2
            top2 = top1
            top1 = [letter, letters[letter]]
        elif letters[letter] >top2[1]:
            top3 = top2
            top2 = [letter, letter[letter]]
        elif letters[letter] > top3[1]:
            top3 = [letter, letters[letter]]
        else:
            pass
    return top1[0], letters[top1[0]]


    



if __name__ == "__main__":
    name = "aabbbccde"
    print(make_logo(name))