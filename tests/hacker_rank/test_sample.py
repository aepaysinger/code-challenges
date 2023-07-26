from code_challenges.hacker_rank.sample import length_of_string


def test_length_of_string():
    assert (
        length_of_string("testing") == 7
    ), f"you should get 7 but got {length_of_string('testing')}"
