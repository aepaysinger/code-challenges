def weight_for_weight(weights):
    weights = weights.split()
    weights = sorted(weights, key=lambda v: sum([int(n) for n in list(v)]))

    i = 0
    j = 1
    while i < len(weights):
        sum_i = sum([int(n) for n in list(weights[i])])
        while j < len(weights) and sum_i == sum([int(n) for n in list(weights[j])]):
            j += 1

        if len(weights[i:j]) > 1:
            for k, num in enumerate(sorted(weights[i:j])):
                weights[i + k] = num

        i = j
        j = i + 1
    return " ".join(weights)


if __name__ == "__main__":
    weights = "103 11 22 20"
    print(weight_for_weight(weights))
