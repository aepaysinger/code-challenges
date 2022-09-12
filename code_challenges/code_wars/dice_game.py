def dice_game(dice_roll):
    points = 0
    if dice_roll.count(1) >= 3:
        points += 1000
        for _ in range(3):
            dice_roll.remove(1)
    elif dice_roll.count(6) >= 3:
        points += 600
        for _ in range(3):
            dice_roll.remove(6)
    elif dice_roll.count(5) >= 3:
        points += 500
        for _ in range(3):
            dice_roll.remove(5)
    elif dice_roll.count(4) >= 3:
        points += 400
        for _ in range(3):
            dice_roll.remove(4)
    elif dice_roll.count(3) >= 3:
        points += 300
        for _ in range(3):
            dice_roll.remove(3)
    elif dice_roll.count(2) >= 3:
        points += 200
        for _ in range(3):
            dice_roll.remove(2)
    for number in dice_roll:
        if number == 1:
            points += 100
        elif number == 5:
            points += 50

    return points


if __name__ == "__main__":
    dice_roll = [2, 4, 4, 5, 4]
    print(dice_game(dice_roll))
