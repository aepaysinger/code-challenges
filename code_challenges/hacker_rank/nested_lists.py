def student_grades(records):
    lowest_score = 100
    second_lowest_score = 100
    lowest_students = []
    second_lowest_students = []
    for student_name_and_score in records:
        if student_name_and_score[1] < lowest_score:
            second_lowest_score = lowest_score
            lowest_score = student_name_and_score[1]
            second_lowest_students = lowest_students
            lowest_students = [student_name_and_score[0]]
        elif student_name_and_score[1] == lowest_score:
            lowest_students.append(student_name_and_score[0])
        elif student_name_and_score[1] < second_lowest_score:
            second_lowest_students = [student_name_and_score[0]]
            second_lowest_score = student_name_and_score[1]
        elif student_name_and_score[1] == second_lowest_score:
            second_lowest_students.append(student_name_and_score[0])
    if second_lowest_students == []:
        return "No Second Lowest"
    else:
        return "\n".join([name for name in sorted((second_lowest_students))])


if __name__ == "__main__":
    # records = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     records.append([name, score])
    print(student_grades([["Ezra", 98.0], ["Oliver", 96.7], ["Rusty", 55.7]]))
