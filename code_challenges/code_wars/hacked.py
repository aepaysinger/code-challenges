def find_hack(student_grades):
    checked_scores = {}
    hacked_students = []

    for name, old_score, grades in student_grades:
        checked_scores[name] = [old_score]
        score = 0
        extra = 0
        for list_of_grades in grades:
            for grade in list_of_grades:
                if grade == "A":
                    score += 30
                    extra += 1
                elif grade == "B":
                    score += 20
                    extra += 1
                elif grade == "C":
                    score += 10
                    extra -= 1
                elif grade == "D":
                    score += 5
                    extra -= 1
                else:
                    extra -= 1
        if extra >= 5:
            score += 20
        checked_scores[name].append(score)
    for student in checked_scores:
        if checked_scores[student][1] > 200:
            hacked_students.append(student)
        elif checked_scores[student][1] != checked_scores[student][0]:
            hacked_students.append(student)

    return hacked_students
