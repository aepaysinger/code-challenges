from code_challenges.code_wars.find_odd_int import FindOddInt


def test_find_odd_int():
    find_odd_int = FindOddInt([1,1,1,1,1,1,10,1,1,1,1])

    assert find_odd_int.find_amount() == 10


def test_find_odd_int_a():
    find_odd_int = FindOddInt([1,2,1,3,1,3,10,1,2,1,1])

    assert find_odd_int.find_amount() == 10