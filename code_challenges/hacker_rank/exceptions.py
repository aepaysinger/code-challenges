def find_the_exception(number_of_test_cases, the_values):
    result =[]
    try:
        for pairs in the_values:
           result.append(int(pairs[0]) / int(pairs[1]))
    except ZeroDivisionError:
        result.append("Error Code: integer division or modulo by zero")
        pass
    except ValueError:
        result.append("Error Code: invalid literal for int() with base 10: '{the_values[1]}'")
    print(result)

if __name__ == "__main__":
    number_of_test_cases = 3
    the_values = [['1', '0'], ['2', '$'], ['3', '1']]
    # for _ in range(number_of_test_cases):
    #     the_values.append(input().split())
    find_the_exception(number_of_test_cases, the_values)