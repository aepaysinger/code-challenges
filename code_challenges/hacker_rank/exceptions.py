def find_the_exception(the_values):
    result = []
    for first, second in the_values:
        try:
            result.append(str(int(int(first) / int(second))))
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
    return "\n".join(result)


if __name__ == "__main__":
    the_values = [["1", "0"], ["2", "$"], ["3", "1"]]
    # for _ in range(number_of_test_cases):
    #     the_values.append(input().split())
    print(find_the_exception(the_values))
