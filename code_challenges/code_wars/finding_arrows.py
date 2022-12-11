def finding_arrows(characters):
    points = 0
    total_points = 0
    for i in range(len(characters)):
        print(characters[i], total_points)
        if characters[i] == ">" and characters[i - 1] == "-" or characters[i -1] == "=":
            total_points += 1
        elif characters[i] == "-":
            total_points += 1
            
            
        
            
    return total_points





if __name__ == "__main__":
    characters = '>===>->'
    print(finding_arrows(characters))