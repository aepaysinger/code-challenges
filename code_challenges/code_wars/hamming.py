def hamming(stra, strb):
    counter = 0
    if len(stra) != len(strb):
        return "The length of the string needs to be the same"
    for i in range(len(stra)):
        if stra[i] != strb[i]:
            counter += 1
    return counter


if __name__ == "__main__":
    stra = "espresso"
    strb = "Expresso"
    print(hamming(stra, strb))
