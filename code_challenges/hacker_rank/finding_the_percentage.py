def finding_the_percentage(name_and_grades, student_query):
    average_grade = sum(name_and_grades[student_query]) / len(
        name_and_grades[student_query]
    )
    return "{:.2f}".format(average_grade)


if __name__ == "__main__":
    name_and_grades = {
        "Krishna": [67.0, 68.0, 69.0],
        "Arjun": [70.0, 98.0, 63.0],
        "Malika": [52.0, 56.0, 60.0],
    }
    student_query = "Malika"
    print(finding_the_percentage(name_and_grades, student_query))
