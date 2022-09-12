def consecutive_strings(starr, k):
    if k > len(starr) or k <= 0 or len(starr) == 0:
        return ""
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
        
    final_words = []
    for i in range(k):
        final_words.append(the_words[i])

    final_string = ""
    for word in starr:
        if word in final_words:
            final_string += word

       
    return  final_string
    
if __name__ == "__main__":
    starr = ["zone", "theta", "abigail", "form", "libe", "zas"]
    k = 2
    print(consecutive_strings(starr, k)) 

   # return in the order they came in"xx