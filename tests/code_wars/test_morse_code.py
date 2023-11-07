from code_challenges.code_wars.morse_code import decode_morse


def test_morse_code_a():
    actual = decode_morse(
        "      ...---... .-- -.--.- -...-   ..--..   ---..   ..-. ..... ... .-- -.-. .--.   .... -.-- --..-- -.-. -....   ....- ....- ...- -....-   .-.. --   .-.-.- ----. .-.-.- -.-.-- -.--.- -- -..-   --.. -...- .... .-.   -.... -.--.- .----. -....- -.--   .---- ---... ..... ----- ..- --..      "
    )
    expected = "SOSW)= ? 8 F5SWCP HY,C6 44V- LM .9.!)MX Z=HR 6)'-Y 1:50UZ"

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_morse_code_b():
    actual = decode_morse(
        "      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.- "
    )
    expected = "SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."

    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_morse_code_c():
    actual = decode_morse(".   .")
    expected = "E E"

    assert actual == expected, f"Returned {actual} instead of {expected}"
