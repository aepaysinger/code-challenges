from code_challenges.code_wars.trigrams import trigrams


def test_trigrams():
    actual = trigrams("the quick red")
    expected = "the he_ e_q _qu qui uic ick ck_ k_r _re red"

    assert actual == expected, f"Returned {actual}, instead of {expected}"


def test_trigrams_a():
    actual = trigrams("hey this is tough")
    expected = "hey ey_ y_t _th thi his is_ s_i _is is_ s_t _to tou oug ugh"

    assert actual == expected, f"Returned {actual}, instead of {expected}"


def test_trigrams_b():
    actual = trigrams("divided by 3")
    expected = "div ivi vid ide ded ed_ d_b _by by_ y_3"

    assert actual == expected, f"Returned {actual}, instead of {expected}"
