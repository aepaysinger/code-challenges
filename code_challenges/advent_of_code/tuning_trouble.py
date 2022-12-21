def get_code():

    with open(
        "./code_challenges/advent_of_code/tuning_trouble_input"
    ) as get_code:
        code = get_code.read()

    return code


def start_of_packet_marker():
    code = get_code()

    window = 4
    for i in range(len(code) - window + 1):
        j = i + window
        slice = code[i:j]
        if len(set(slice)) == 4:
            return j


def start_of_packet_message():
    code = get_code()
    window = 14

    for i in range(len(code) - window + 1):
        j = i + window
        slice = code[i:j]
        if len(set(slice)) == 14:
            return j


print(get_code())
print(start_of_packet_marker())
print(start_of_packet_message())
