def consecutive_strings(starr, k):
    word_tracker = {}
    
    for word in starr:
        if word_tracker.get(len(word)) == None:
            word_tracker[len(word)] = [word]
        else:
            word_tracker[len(word)] += [word]
    print(word_tracker)
    
    the_words = []

    
    for _ in range(len(word_tracker)):
        amount = 0
        for word_length in word_tracker:
            if word_length > amount:
                amount = word_length
        the_words += word_tracker[amount]
        del word_tracker[amount]
        amount = 0
        
       
    
    final_string = ""
    for i in range(k):
        final_string += the_words[i]
       
    return  final_string
    
if __name__ == "__main__":
    starr = ["zone", "abigail", "theta", "form", "libe", "zas"]
    k = 2
    print(consecutive_strings(starr, k)) 