def code_device():
    with open(
        "/Users/amelia/projects/code-challenges/code_challenges/advent_of_code/device_input"
    ) as code:
        device_code = code.read().split("\n")
    device_code = [line.split(" ") for line in device_code]
    return device_code


def build_directories():
    device_code = code_device()
    computer_directories = {"/": {}}
    directory_name = [] # [/]
    directory_level = 0
    for i, line in enumerate(device_code):
        if len(line) == 3 and line[1] == "cd":
            directory_name.append(line[2])
        elif len(line) == 2 and line[1] == "ls":
            continue
        elif len(line) == 2 and line[0] == dir:
            computer_directories[directory_name[directory_level]].update(line[1], [])
            directory_name.append(line[1])
        elif len(line) == 2:
            computer_directories[old_directory_name][new_directory_name].append([line[0], line[1]])


    return computer_directories

$ cd / 
$ ls (skipped)
dir a 
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
                
                
print(build_directories())