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
        "X": 10,
        "/": 10,
    }
    for i, round in enumerate(frames):
        if round[0] == "x":
            
        score += points[round[0]] + points[round[0]]
        print(score)
        
        

    return frames


if __name__ == "__main__":
    frames = "11 11 11 11 11 11 11 11 11 11"
    print(bowling_score(frames))