import re


def detect_floating_point_number(cases):
    results = []
    for case in cases:
        if re.search("[a-zA-Z]", case):
            results.append("False")
            continue
        if case[0] == "-" or case[0] == "+":
            case = case[1:]
        if "+" in case or case.isalpha() or "-" in case:
            results.append("False")
        elif case.count(".") != 1:
            results.append("False")
        else:
            results.append("True")

    return "\n".join(results)


if __name__ == "__main__":
    cases = ["+3.35567", "-976.676", "+54.4+44", "+8753", "--8754"]
    print(detect_floating_point_number(cases))
