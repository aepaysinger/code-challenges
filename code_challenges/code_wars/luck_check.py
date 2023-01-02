def luck_check(numbers):
    if numbers == "":
        raise ValueError("empty string")
    if numbers.isdigit():
        if len(numbers) % 2 == 0:
            first_half = numbers[: int(len(numbers) / 2)]
            second_half = list(numbers[int(len(numbers) / 2) :])
            second_half_total = 0
            for number in second_half:
                second_half_total += int(number)
            first_half_total = 0
            for number in first_half:
                first_half_total += int(number)
        else:
            first_half = numbers[: int(len(numbers) / 2)]
            second_half = list(numbers[int(len(numbers) / 2) + 1 :])
            second_half_total = 0
            for number in second_half:
                second_half_total += int(number)
            first_half_total = 0
            for number in first_half:
                first_half_total += int(number)

        return first_half_total == second_half_total
    else:
        raise ValueError("needs to be numbers")


if __name__ == "__main__":
    numbers = "3g456"
    print(luck_check(numbers))
