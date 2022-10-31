from code_challenges.code_wars.maximum_subarray_sum import max_sequence


# def test_max_sequence():
#     actual = max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
#     expected = 6

#     assert actual == expected, f"Returned {actual} instead of {expected}."


# def test_max_sequence_all_negative():
#     actual = max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4])
#     expected = 0

#     assert actual == expected, f"Returned {actual} instead of {expected}."


# def test_max_sequence_empty():
#     actual = max_sequence([])
#     expected = 0

#     assert actual == expected, f"Returned {actual} instead of {expected}."

# def test_max_sequence_A():
#     actual = max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43])
#     expected = 155

#     assert actual == expected, f"Returned {actual} instead of {expected}."

def test_max_sequence_B():
    actual = max_sequence([1,2,3,-4,5,6,7])
    expected = [(0,2),(0,6),(4,6)]
    assert actual == expected, f"{actual} != {expected}"
    