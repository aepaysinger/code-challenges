from code_challenges.code_wars.trigrams import trigrams


def test_trigrams():
    actual = trigrams("the quick red")
    expected = "the he_ e_q _qu qui uic ick ck_ k_r _re red"

    assert actual == expected, f"Returned {actual}, instead of {expected}"
    