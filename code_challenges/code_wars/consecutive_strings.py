def consecutive_strings(starr, k):
    word_tracker = {}
    
    for word in starr:
        if word_tracker.get(len(word)) == None:
            word_tracker[len(word)] = [word]
        else:
            word_tracker[len(word)] += [word]

    longest = 0
    consecutive_string = ""
    

       
    return word_tracker, consecutive_string

    




if __name__ == "__main__":
    starr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
    k = 2
    print(consecutive_strings(starr, k)) 