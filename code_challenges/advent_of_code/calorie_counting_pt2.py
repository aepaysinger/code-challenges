def get_elves_calories_top_3():
    calories = open("/Users/amelia/projects/code-challenges/code_challenges/advent_of_code/calorie_counting_input")
    elves_calories = calories.read().split("\n\n")
    calories.close()

    with open("/Users/amelia/projects/code-challenges/code_challenges/advent_of_code/calorie_counting_input") as calories:
        elves_calories = calories.read().split("\n\n")

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
print(get_elves_calories_top_3())


# if __name__ == "__main__":
#     elves_calories = ['1000,2000,3000', '4000', '5000,6000', '7000,8000,9000', '10000']
#     print(get_elves_calories_top_3(elves_calories))