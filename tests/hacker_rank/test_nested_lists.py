from code_challenges.hacker_rank.nested_lists import student_grades


def test_student_grades_tie():                   
    actual = student_grades([['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]])                                  
                    
    assert actual == 'Berry\nHarry', f"Returned: {actual}, instead of Berry\nHarry'"