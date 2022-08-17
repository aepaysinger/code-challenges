def find_outlier(numbers):
    odd_and_even = {
        "odd": [],
        "even": [],
    }
    for number in numbers:
        if number % 2 == 0:
            odd_and_even["even"].append(number)
        else:
            odd_and_even["odd"].append(number)
    if len(odd_and_even["odd"]) == 1:
        return odd_and_even["odd"][0]
    else:
        return odd_and_even["even"][0]


if __name__ == "__main__":
    numbers = [34, 68, 11, 102, 14]
    print(find_outlier(numbers))
