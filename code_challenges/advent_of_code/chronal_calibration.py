def frequency_input():
    with open(
        "./code_challenges/advent_of_code/frequency_input"
    ) as different_frequencies:
        frequencies = different_frequencies.read().split("\n")

    return frequencies

def find_final_frequency():
    frequencies = frequency_input()
    final_frequency = 0

    for frequency in frequencies:
        if frequency[0] == "+":
            final_frequency += int(frequency[1:])
        elif frequency[0] == "-":
            final_frequency -= int(frequency[1:])
    return final_frequency

def visited_frequency_twice():
    frequencies = frequency_input()
    current_frequency = 0
    visited_frequencies = []
    visited_twice = None
    while visited_twice == None:
        for frequency in frequencies:
            # print(current_frequency, visited_frequencies)
            if frequency[0] == "+":
                current_frequency += int(frequency[1:])
                if current_frequency not in visited_frequencies:
                    visited_frequencies.append(current_frequency)
                else:
                    visited_twice = current_frequency
            elif frequency[0] == "-":
                current_frequency -= int(frequency[1:])
                if current_frequency not in visited_frequencies:
                    visited_frequencies.append(current_frequency)
                else:
                    visited_twice = current_frequency
    return visited_twice

    # print(len(visited_frequencies))
    # updated_visited_frequencies = set(visited_frequencies)
    # print(len(updated_visited_frequencies))

    

# print(frequency_input())
# print(find_final_frequency())
print(visited_frequency_twice())
