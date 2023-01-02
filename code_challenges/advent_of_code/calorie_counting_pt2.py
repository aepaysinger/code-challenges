def elves_input():
    with open(
        "./code_challenges/advent_of_code/calorie_counting_input"
    ) as calories:
        elves_calories = calories.read().split("\n\n")

    return elves_calories


def get_elves_calories_top_3():
    elves_calories = elves_input()

    highest_elf_calorie_1 = 0
    highest_elf_calorie_2 = 0
    highest_elf_calorie_3 = 0
    elves_calories = [elf_calorie.replace("\n", ",") for elf_calorie in elves_calories]
    for elf_calorie in elves_calories:
        elf_calorie = elf_calorie.split(",")
        elf_calorie = [int(amount) for amount in elf_calorie]
        elf_calorie = sum(elf_calorie)
        if elf_calorie > highest_elf_calorie_3:
            highest_elf_calorie_1 = highest_elf_calorie_2
            highest_elf_calorie_2 = highest_elf_calorie_3
            highest_elf_calorie_3 = elf_calorie
        elif elf_calorie > highest_elf_calorie_2:
            highest_elf_calorie_1 = highest_elf_calorie_2
            highest_elf_calorie_2 = elf_calorie
        elif elf_calorie > highest_elf_calorie_1:
            highest_elf_calorie_1 = elf_calorie

    return highest_elf_calorie_1 + highest_elf_calorie_2 + highest_elf_calorie_3
