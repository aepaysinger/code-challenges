def spreadsheet_input():
    with open(
        "./code_challenges/advent_of_code/spreadsheet_input"
    ) as numbers:
        spread_sheet = numbers.read().split("\t")
    spread_sheet_result = []
    holding = []
    for numbers in spread_sheet:
        pause = ""
        if "\n" in numbers:
            for number in numbers:
                if number == "\n":
                    holding.append(pause)
                    
                else:
                    pause += number
                    
            # print(number[:None], number[None:])
            # holding.append(number[:None])
            # spread_sheet_result.append(holding)
            # holding = []
            # holding.append(number[None:])
        else:
            holding.append(number)
        

    return spread_sheet_result

print(spreadsheet_input())