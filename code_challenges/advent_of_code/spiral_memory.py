def steps_to_center(final_number):
    steps_and_their_numbers = {}
    break_point = 10
    difference = 16
    even_distance = 1
    odd_distance = 2
    for number in range(2, final_number):
        if number < break_point:
            if number % 2 == 0:
                steps_and_their_numbers[even_distance] = steps_and_their_numbers.get(
                    even_distance, []
                ) + [number]
            else:
                steps_and_their_numbers[odd_distance] = steps_and_their_numbers.get(
                    odd_distance, []
                ) + [number]
        if number == break_point:
            print(number)
            even_distance += 2
            odd_distance += 2
            steps_and_their_numbers[even_distance] = steps_and_their_numbers.get(
                even_distance, []
            ) + [number]
            break_point += difference
            difference += 8

    return steps_and_their_numbers


print(steps_to_center(26))
