def device_code():
    with open(
        "/Users/amelia/projects/code-challenges/code_challenges/advent_of_code/device_input"
    ) as code:
        device_code = code.read().split("\n")
    device_code = [line.split(" ") for line in device_code]
    return device_code


def build_directories():
    device_code = device_code()
    computer_directories = {}
    for i, line in enumerate(device_code):
        if len(line) == 2:
            if line[0] == "ls":
                
                
print(device_code())