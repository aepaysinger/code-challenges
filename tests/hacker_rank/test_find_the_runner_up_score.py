from code_challenges.hacker_rank.find_the_runner_up_score import runner_up
from code_challenges.hacker_rank.find_the_runner_up_score import check_tie


def test_runner_up_low_first():                    
    actual = runner_up([2, 3, 6, 6, 5])                                 
    expected = 5                   

    assert actual == expected, f"Returned: {actual}, instead of {expected}"


def test_runner_up_tie():                    
    actual = runner_up([8, 8, 8, 8])                                 
    expected = "it's a tie!"                   

    assert actual == expected, f"Returned: {actual}, instead of {expected}"


def test_runner_up_high_first():                    
    actual = runner_up([7, 6, 3, 3, 5])                                 
    expected = 6                   

    assert actual == expected, f"Returned: {actual}, instead of {expected}"


def test_check_tie_true():
    actual = check_tie([3, 3, 3, 3])
    expected = True

    assert actual == expected, f"Returned: {actual}, instead of {expected}"


def test_check_tie_false():
    actual = check_tie([1, 2, 3, 3])
    expected = False

    assert actual == expected, f"Returned: {actual}, instead of {expected}"
 