def elves_input():
    with open("./code_challenges/adhoc/calorie_counting_input") as calories:
        elves_calories = calories.read().split("\n\n")
    return elves_calories


def get_elves_calories():
    elves_calories = elves_input()

    highest_elf_calorie = 0
    elves_calories = [elf_calorie.replace("\n", ",") for elf_calorie in elves_calories]
    for elf_calorie in elves_calories:
        elf_calorie = elf_calorie.split(",")
        elf_calorie = [int(amount) for amount in elf_calorie]
        elf_calorie = sum(elf_calorie)
        if elf_calorie > highest_elf_calorie:
            highest_elf_calorie = elf_calorie

    return highest_elf_calorie
