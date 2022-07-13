from itertools import combinations

from code_challenges.hacker_rank.itertools_combinations import making_combinations


def test_making_combinations():
    actual = making_combinations('ABCD', 3)
    expected = list(combinations("ABCD", 3))
    assert actual == expected, f"Returned: {actual}, instead of {expected}"

    #  reps = 4
    # expected = "".join([f"{i*i}\n" for i in range(reps)])