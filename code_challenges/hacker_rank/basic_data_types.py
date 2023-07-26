def basic_data_types(commands):
    result = []
    for command in commands:
        if command[0] == "insert":
            result.insert(int(command[1]), int(command[2]))
        if command[0] == "print":
            print(result)
        if command[0] == "remove":
            result.remove(int(command[1]))
        if command[0] == "append":
            result.append(int(command[1]))
        if command[0] == "sort":
            result.sort()
        if command[0] == "pop":
            result.pop()
        if command[0] == "reverse":
            result.reverse()


if __name__ == "__main__":
    commands = [
        ["insert", "0", "5"],
        ["insert", "1", "10"],
        ["insert", "0", "6"],
        ["print"],
        ["remove", "6"],
        ["append", "9"],
        ["append", "1"],
        ["sort"],
        ["print"],
        ["pop"],
        ["reverse"],
        ["print"],
    ]
    basic_data_types(commands)
