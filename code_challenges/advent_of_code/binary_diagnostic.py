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
    return int(gamma_rate,2) * int(epsilon_rate,2)


def life_support_rating():
    diagnostic_report = get_diagnostic_report()
    zeroes = []
    ones = []
    
    for numbers in diagnostic_report:
        if numbers[0] == "0":
            zeroes.append(numbers)
        else:
            ones.append(numbers)
    while len(zeroes) != 1:
        zeroes_holding = []
        for numbers in zeroes:
            if numbers[0] == "0":
                zeroes_holding.append(numbers)
        zeroes = zeroes_holding  
    while len(ones) != 1:
        ones_holding = []
        for numbers in ones:
            if numbers[0] == "1":
                ones_holding.append(numbers)
        ones = ones_holding
    return zeroes, ones
    

# print(get_diagnostic_report())
# print(find_submarine_power_consumption())
print(life_support_rating())