from code_challenges.code_wars.finding_arrows import finding_arrows


def test_finding_arrows_a():
    actual = finding_arrows('>.')
    expected = 1

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_finding_arrows_b():
    actual = finding_arrows("<--..")
    expected = -3

    assert actual == expected, f"Returned {actual} instead of {expected}"



def test_finding_arrows_c():
    actual = finding_arrows('><=><--')
    expected = -2

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_finding_arrows_d():
    actual = finding_arrows('>===>->')
    expected = 11

    assert actual == expected, f"Returned {actual} instead of {expected}"



def test_finding_arrows_e():
    actual = finding_arrows('<-->')
    expected = 0

    assert actual == expected, f"Returned {actual} instead of {expected}"