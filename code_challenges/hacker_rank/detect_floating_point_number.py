def detect_floating_point_number(cases):
    results = []
    for case in cases:
        if "+" in case[1:]:
            results.append("False")
        if case.isalpha():
            results.append("False")   
        if case[0] == "-" or case[0] == "+":
            case = case.replace('-', '')
            case = case.replace('+', '')
        elif case.isdigit():
            results.append("False")
        else:
            results.append("True")
        
    return  "\n".join(results)
        

if __name__ == "__main__":
    cases = ["1.414", "+.5486468", "0.5.0", "1+1.0", "0"]
    print(detect_floating_point_number(cases))


# def detect_floating_point_number(cases):
#     results = []
#     for case in cases:
#         if "+" in case[1:]:
#             results.append("False")
#         if case.isalpha():
#             results.append("False")   
#         if case[0] == "-" or "+":
#             case = case.replace('-', '')
#             case = case.replace('+', '')
#             try:
#                 if float(case):
#                     results.append("True")
#             except ValueError:
#                 results.append("False")
        
#     return  "\n".join(results)
