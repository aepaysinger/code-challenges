def find_the_exception(number_of_test_cases, the_values):
    result = []
    for first, second in the_values:
        try:
            result.append(int(int(first) / int(second)))
        except ZeroDivisionError:
            result.append("Error Code: integer division or modulo by zero")
        except ValueError:
            if first.isdigit():
                result.append(
                    f"Error Code: invalid literal for int() with base 10: '{second}'"
                )
            else:
                result.append(
                    f"Error Code: invalid literal for int() with base 10: '{first}'"
                )
    return "\n".join(map(str, result))


if __name__ == "__main__":
    number_of_test_cases = int(input())
    the_values = []
    for _ in range(number_of_test_cases):
        the_values.append(input().split())
    print(find_the_exception(number_of_test_cases, the_values))
