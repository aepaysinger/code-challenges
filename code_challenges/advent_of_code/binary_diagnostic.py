def get_diagnostic_report():
    with open("./code_challenges/advent_of_code/diagnostic_report_input") as numbers:
        diagnostic_report = numbers.read().split("\n")
    return diagnostic_report


def find_submarine_power_consumption():
    diagnostic_report = get_diagnostic_report()
    gamma_rate = ""
    epsilon_rate = ""

    for i in range(len(diagnostic_report[0])):
        zero = 0
        one = 0
        for numbers in diagnostic_report:
            if numbers[i] == "0":
                zero += 1
            else:
                one += 1
        if zero > one:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def life_support_rating():
    diagnostic_report = get_diagnostic_report()
    zeroes = []
    ones = []

    for numbers in diagnostic_report:
        if numbers[0] == "0":
            zeroes.append(numbers)
        else:
            ones.append(numbers)
    print(zeroes, ones)
    if len(zeroes) > len(ones):
        oxygen = zeroes
    else:
        oxygen = ones
    to_match = oxygen[0][1]
    i = 1
    while len(oxygen) != 1:
        oxygen_holding = []
        other_holding = []
        for numbers in oxygen:
            if numbers[i] == to_match:
                oxygen_holding.append(numbers)
            else:
                other_holding.append(numbers)
        if len(oxygen_holding) > len(other_holding):
            oxygen = oxygen_holding
        elif len(oxygen_holding) == len(other_holding) and len(oxygen_holding) != 1:
            if oxygen_holding[0][i] == "1":
                oxygen = oxygen_holding
            else:
                oxygen = other_holding
        else:
            oxygen = other_holding
        if len(oxygen) == 1:
            break
        i += 1
        to_match = oxygen[0][i]

    if len(zeroes) < len(ones):
        c02 = zeroes
    else:
        c02 = ones
    to_match = c02[0][1]
    i = 1
    print(c02)
    while len(c02) != 1:
        c02_holding = []
        other_holding = []
        for numbers in c02:
            if numbers[i] == to_match:
                c02_holding.append(numbers)
            else:
                other_holding.append(numbers)
        print(f"c02: {c02_holding},other: {other_holding}, {i}")
        if len(c02_holding) < len(other_holding):
            c02 = c02_holding
        elif len(c02_holding) == len(other_holding) and len(c02_holding) != 1:
            if c02_holding[0][i] == "0":
                c02 = c02_holding
            else:
                c02 = other_holding
        else:
            c02 = other_holding
        # print(c02, i)
        if len(c02) == 1:
            break
        i += 1
        to_match = c02[0][i]

    return int(oxygen[0], 2) * int(c02[0], 2)


# print(get_diagnostic_report())
# print(find_submarine_power_consumption())
print(life_support_rating())
