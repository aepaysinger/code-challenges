def code_device():
    with open(
        "/Users/amelia/projects/code-challenges/code_challenges/advent_of_code/device_input"
    ) as code:
        device_code = code.read().split("\n")
    device_code = [line.split(" ") for line in device_code]
    return device_code


# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e

class FileSystem:
    def __init__(self, device_code):
        self.root = Directory(device_code[0][2])
        self.current = self.root
        
        for line in device_code[1:]:

            if len(line) == 3 and line[1] == "cd" and line[2] != "..":
                dir = Directory(line[2], parent=self.current)
                self.curent.children.append(dir)
                self.current = dir
            if len(line) == 3 and line[1] == "cd" and line[2] == "..":
                self.current = self.current.parent
            



class Directory:
    def __init__(self, location, parent=None):
        self.location = location
        self.parent = parent
        self.children = []
        self.files = []
    
    def (self):
        pass


def build_directories():
    device_code = code_calculate_sizedevice()
    computer_directories = {"/": {}} # {"/": "a": {"e": {"i": 584}, "f": 29116, "g": 2557, "h.lst": 62596}, "b.txt": 14848514, "c.dat": 8504156, "d": {"j": 4060174}}
    directory_name = [] # /, a, d, e
    directory_level = 0 # 0, 1, 3, 2, 1, 2
    for i, line in enumerate(device_code):
        print(computer_directories)
        if len(line) == 3 and line[1] == "cd":
            if line[2] == "..":
                directory_level -= 1
                continue
            if line[2] not in directory_name:
                directory_name.append(line[2])
            directory_level = directory_name.index(line[2])
        elif len(line) == 2 and line[1] == "ls":
            continue
        elif len(line) == 2 and line[0] == "dir":
            computer_directories[directory_name[directory_level]].update({line[1]: {}})
            directory_name.append(line[1])
        elif len(line) == 2:
            computer_directories[directory_name[directory_level]].update({line[1]: int(line[0])})


    return computer_directories


# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
#  dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
                
                
print(build_directories())