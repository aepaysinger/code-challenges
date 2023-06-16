def get_segments():
    with open("code_challenges/advent_of_code/segments_input") as segment_input:
        segments = segment_input.read().split("\n")
    return [segment.split("|") for segment in segments]


def find_1_4_7_8():
    segments = get_segments()
    numbers = {}
    for segment_input, segment_output in segments:
        for segment in segment_output.split(" "):
            numbers[len(segment)] = numbers.get(len(segment), 0) + 1
    return numbers[2] + numbers[4] + numbers[3] + numbers[7]

def find_output_values():
    segments = get_segments()
    total = 0
    for segment_input, segment_output in segments:
        segment_total = ""
        for segment in segment_output.split(" "):
            if len(segment) == 2:
                segment_total += "1"
            elif len(segment) == 4:
                segment_total += "4"
            elif len(segment) == 3:
                segment_total += "7"
            elif len(segment) == 7:
                segment_total += "8"
            elif len(segment) == 5 and ''.join(sorted(segment)) == "bcdef":
                segment_total += "5"
            elif len(segment) == 5 and ''.join(sorted(segment)) == "acdfg":
                segment_total += "2"
            elif len(segment) == 5 and ''.join(sorted(segment)) == "abcdf":
                segment_total += "3"
            elif len(segment) == 6 and ''.join(sorted(segment)) == "abcdef":
                segment_total += "9"
            elif len(segment) == 6 and ''.join(sorted(segment)) == "abcdfg":
                segment_total += "6"
            elif len(segment) == 6 and ''.join(sorted(segment)) == "abcdeg":
                segment_total += "0"
            print(segment, segment_total)
        segment_total = int(segment_total)
        total += segment_total
    
    return total
                

# print(get_segments())
# print(find_1_4_7_8())
print(find_output_values())