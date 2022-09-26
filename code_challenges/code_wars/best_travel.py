from itertools import combinations
from multiprocessing.connection import wait


def best_travel(number_of_destinations, total_miles, destination_miles):
    find_miles(destination_miles, number_of_destinations)
    wanted_mile_combos = remove_unwanted_miles(total_miles)
    top_combo = None
    top_miles = 0
    for mile_combo in wanted_mile_combos:
        if wanted_mile_combos[mile_combo] >= top_miles:
            top_combo = mile_combo
            top_miles = wanted_mile_combos[mile_combo]
    return top_miles
    


def find_miles(destination_miles, number_of_destinations):
    destination_totals = {}
    combos = combinations(destination_miles, number_of_destinations)
    for i in list(combos):
        destination_totals[i] = sum(list(i))

    return destination_totals

def remove_unwanted_miles(total_miles):
    all_mile_combos = find_miles(destination_miles, number_of_destinations)
    wanted_mile_combos = {}
    for mile_combos in all_mile_combos:
        if all_mile_combos[mile_combos] <= total_miles:
            wanted_mile_combos[mile_combos] = all_mile_combos[mile_combos]

    return wanted_mile_combos




if __name__ == "__main__":
    number_of_destinations = 3
    total_miles = 174
    destination_miles = [50, 55, 57, 58, 60]
    print(best_travel(number_of_destinations, total_miles, destination_miles))