def opcode_integers():
    with open("./code_challenges/advent_of_code/opcode_input") as integers:
        opcode = integers.read().split(",")

    return [int(integer) for integer in opcode]


def get_next_noun_verb_pair():
    for i in range(100):
        for j in range(100):
            noun = i
            verb = j
            pair = (noun, verb)
            yield pair
    raise StopIteration


def opcode_instructions(output):
    opcode = opcode_integers()
    step = 4
    opcode_results = opcode.copy()
    pairs = get_next_noun_verb_pair()

    while opcode_results[0] != output:
        try:
            noun, verb = next(pairs)
        except StopIteration:
            break
        opcode_results = opcode.copy()
        opcode_results[1] = noun
        opcode_results[2] = verb
        i = 0

        while opcode_results[i] != 99:
            a = opcode_results[i + 1]
            b = opcode_results[i + 2]
            c = opcode_results[i + 3]
            if opcode_results[i] == 1:
                result = opcode_results[a] + opcode_results[b]
                opcode_results[c] = result
            if opcode_results[i] == 2:
                result = opcode_results[a] * opcode_results[b]
                opcode_results[c] = result
            i += step
    return noun, verb


def final_result():
    noun, verb = opcode_instructions()

    return 100 * noun + verb
