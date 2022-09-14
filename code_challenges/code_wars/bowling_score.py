def bowling_score(frames):
    frames = frames.split(" ")
    score = 0
    points = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    for i, round in enumerate(frames):
        if len(frames[i]) == 2:
            if frames[i][1] == "/":
                score += 10 + (points[frames[i+1][0]])
            else:
                score += points[frames[i][0]] + points[frames[i][1]]
        if len(frames[i]) == 3:
            if frames[i] == "XXX":
                score += 30
        if frames[i] == "X":
            if i == 7:
                if frames[i+1] == "X" and frames[i+2][0] == "X":
                    score += 30
                    
            if i == 8:    
                if frames[i+1][0] == "X" and frames[i+1][1] == "X":
                    score += 30
                    
            # if i == 9:
            #     if frames[i+1][0] == "X" and frames[i+1][1] == "X" and frames[i+1][2] == "X":
            #         score += 30
            elif frames[i+1] == "X" and frames[i+2] == "X":
                score += 30
            elif frames[i+1] == "X":
                score += 20
            elif frames[i+1] != "X" and i != 7 or 8 or 9:
                score += 10 + (points[frames[i+1][0]] + points[frames[i+1][1]])
        print(frames[i], i, score)
    return score


if __name__ == "__main__":
    frames = "X X X X X X X X X XXX"
    print(bowling_score(frames))