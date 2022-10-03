from code_challenges.adhoc.counter import Counter


def test_counter_increment():
    counter = Counter()

    assert counter.value() == 0

    counter.increment()

    assert counter.value() == 1

    counter.increment()

    assert counter.value() == 2


def test_counter_decrement():
    counter = Counter()

    assert counter.value() == 0

    counter.decrement()

    assert counter.value() == -1
