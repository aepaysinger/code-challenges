import pytest

from code_challenges.adhoc.random_num_generator import RandomNumGenerator


def test_random_num_generator():
    random_num_gen = RandomNumGenerator(1, 5)

    assert random_num_gen.get() in range(1, 6)


def test_random_num_generator_no_repeat():
    random_num_gen = RandomNumGenerator(1, 5)
    random_nums = set()
    for _ in range(5):
        random_nums.add(random_num_gen.get())
    
    assert len(random_nums) == 5
        
    
def test_random_num_generator_too_many():
    random_num_gen = RandomNumGenerator(1, 5)
    random_nums = set()
    with pytest.raises(ValueError):
        for _ in range(6):
            random_nums.add(random_num_gen.get())
