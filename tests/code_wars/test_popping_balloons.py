from code_challenges.code_wars.popping_balloons import Balloons, freq_stack


def test_popping_balloons_4_pops():
    actual = freq_stack(4, [5, 7, 5, 7, 4, 5])
    expected = [5, 7, 5, 4]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_popping_balloons_10_pops():
    actual = freq_stack(10, [1, 2, 3, 4, 5, 5, 7, 8, 9, 10])
    expected = [5, 10, 9, 8, 7, 5, 4, 3, 2, 1]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_popping_balloons_5_pops():
    actual = freq_stack(5, [1, 1, 1, 10, 5, 5, 10, 7, 8])
    expected = [1, 10, 5, 1, 8]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_popping_balloons_7_pops():
    actual = freq_stack(7, [12, 9, 8, 8, 12, 12, 6, 1, 8])
    expected = [8, 12, 12, 8, 1, 6, 8]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_popping_balloons_multiple_same_amount():
    actual = freq_stack(3, [1, 2, 3, 2, 1, 3, 4, 2, 1, 3])
    expected = [3, 1, 2]

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_track_balloons():
    balloons = Balloons([5, 7, 5, 7, 4, 5])

    assert balloons.track_balloons() == {5: 3, 7: 2, 4: 1}


def test_find_top_balloon():
    balloons = Balloons([5, 7, 5, 7, 4, 5])
    balloons.track_balloons()

    assert balloons.find_top_balloons() == (5, 3)


def test_pop_most_1():
    balloons = Balloons([5, 7, 5, 7, 4, 5])
    balloons.track_balloons()
    balloons.find_top_balloons()
    balloons.pop_most(1)

    assert balloons.popped_ballons == [5]
    assert balloons.balloons_amount == {5: 2, 7: 2, 4: 1}


def test_pop_most_2():
    balloons = Balloons([5, 7, 5, 7, 4, 5])
    balloons.track_balloons()
    balloons.find_top_balloons()
    balloons.pop_most(2)

    assert balloons.popped_ballons == [5, 7]
    assert balloons.balloons_amount == {5: 2, 7: 1, 4: 1}


def test_pop_most_4():
    balloons = Balloons([5, 7, 5, 7, 4, 5])
    balloons.track_balloons()
    balloons.find_top_balloons()
    balloons.pop_most(4)

    assert balloons.popped_ballons == [5, 7, 5, 4]
    assert balloons.balloons_amount == {5: 1, 7: 1, 4: 1}
