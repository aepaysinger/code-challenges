def encode(st):
    final = ""
    for i in range(0, len(st), 2):
        final += st[i + 1] * int(st[i])
    return final        
    
def decode(st): 
    final = ""
    count = 0
    current = st[0]
    for character in st:
        if character != current:
            final += str(count) + current
            current = character
            count = 1
        else:
            count += 1
    final += str(count) + current

    return final


if __name__ == "__main__":
    st = "AAABBBCCCA"
    # print(encode(st))
    print(decode(st))

#"AAABBBCCCA"
"3A3B3C1A" 