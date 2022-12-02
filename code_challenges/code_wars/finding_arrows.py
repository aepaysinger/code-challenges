def finding_arrows(characters):
    points = 0
    total_points = 0
    for i in range(len(characters)):
        print(characters[i], points)
        if characters[i] == ">":
            total_points += 1
        elif characters[i] == "-":
            
            
        
            
    return total_points





if __name__ == "__main__":
    characters = '>===>->'
    print(finding_arrows(characters))