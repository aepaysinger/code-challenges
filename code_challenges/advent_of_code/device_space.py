def device_code():
    with open(
        "/Users/amelia/projects/code-challenges/code_challenges/advent_of_code/device_input"
    ) as code:
        device_code = code.read().split("\n")
    device_code = [line.split(" ") for line in device_code]
    return device_code

print(device_code())