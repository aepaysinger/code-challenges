def get_segments():
    with open("code_challenges/advent_of_code/segments_input") as segment_input:
        segments = segment_input.read().split("\n")
    return [segment.split("|") for segment in segments]


def find_1_4_7_8():
    segments = get_segments()
    numbers = {}
    for segment_input, segment_output in segments:
        segment_out = segment_output.split(" ")
        print(segment_output)

# print(get_segments())
print(find_1_4_7_8())