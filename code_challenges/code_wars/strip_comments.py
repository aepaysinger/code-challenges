def strip_comments(k, markers):
    for i, item in enumerate(markers):
        final_result = k.replace(item[i], "")
    
        print(final_result)
    return 




if __name__ == "__main__":
    k = "apples, pears # and bananas\ngrapes\nbananas !apples"
    markers = ['!', '#']
    print(strip_comments(k, markers))
    