# a function that takes a list of numbers and adds together the two most frequently accuring numbers and returns them
def sum_most_frequent_numbers(numbers):
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    num_a = 0
    num_a_count = 0
    num_b = 0
    num_b_count = 0
    for number in counts:
        if counts[number] >= num_a_count:
            num_b = num_a
            num_b_count = num_a_count
            num_a = number
            num_a_count = counts[number]
        elif counts[number] >= num_b_count:
            num_b_count = counts[number]
            num_b = number

    return num_a + num_b


if __name__ == "__main__":
    l = [1, 4, 3, 3, 7, 2, 2, 9]
    print(sum_most_frequent_numbers(l))
