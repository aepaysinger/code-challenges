import itertools


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
    visited_frequencies = set()

    for frequency in itertools.cycle(frequencies):
        if frequency[0] == "+":
            current_frequency += int(frequency[1:])
        elif frequency[0] == "-":
            current_frequency -= int(frequency[1:])

        if current_frequency in visited_frequencies:
            return current_frequency
        visited_frequencies.add(current_frequency)
