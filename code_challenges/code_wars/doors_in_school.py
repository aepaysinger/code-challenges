class SchoolDoors():
    def __init__(self, students):
        self.students = students
        self.door_tracker = {}
        for student in range(1, students+1):
            self.door_tracker[student] = "closed"

    def go_through_doors(self):
        for student in range(1, self.students + 1):
            for door in self.door_tracker:
                if door % student == 0:
                    if self.door_tracker[door] == "open":
                        self.door_tracker[door] = "closed"
                    elif self.door_tracker[door] == "closed":
                        self.door_tracker[door] = "open"
        return self.door_tracker

    def count_open_doors(self):
        open_count = 0
        for door in self.door_tracker:
            if self.door_tracker[door] == "open":
                open_count += 1
        return open_count

def doors(students):
    school_doors = SchoolDoors(students)
    school_doors.go_through_doors()

    return school_doors.count_open_doors()


if __name__ == "__main__":
    students = 5
    print(doors(students))



    

