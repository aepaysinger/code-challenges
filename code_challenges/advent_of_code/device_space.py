def code_device():
    with open(
        "/Users/amelia/projects/code-challenges/code_challenges/advent_of_code/device_input"
    ) as code:
        device_code = code.read().split("\n")
    device_code = [line.split(" ") for line in device_code]
    return device_code


def build_directories():
    device_code = code_device()
    computer_directories = {"/": None}
    directory_name = ""
    for i, line in enumerate(device_code):
        if len(line) == 3:
            if line[1] == "cd":
                directory_name = line[2]
        elif len(line) == 2 and line[0] == "dir":
            # computer_directories[directory_name].update({line[1]: []})
            computer_directories[directory_name] = {line[1]: []}
            directory_name = {line[1]}
        elif len(line) == 2 and line[1] == "ls":
            continue
        elif len(line) == 2:
            continue
            # computer_directories[directory_name] = computer_directories.get(line[1])

    return computer_directories


                
                
print(build_directories())