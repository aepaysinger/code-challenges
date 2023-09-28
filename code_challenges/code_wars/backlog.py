def legal_backlog(cases, max_daily_sessions):
    days = 0
    daily_sessions = max_daily_sessions if max_daily_sessions < len(cases) else len(cases)
    count = 0
    case_names = sorted([case for case in cases], key=lambda case: cases[case], reverse=True)
    case_to_check = 0
    # print(case_to_check)
    while cases:
        
        # print(cases, days)
        for i in range(daily_sessions):
            # if cases == {}:
            #     return days
            
            if case_to_check > len(cases) - 1:
                case_to_check = 0
            # print(case_names, i)
            if cases[case_names[case_to_check]] > 0:
                cases[case_names[case_to_check]] -= 1
                if cases[case_names[case_to_check]] == 0:
                    for case in case_names:
                        if cases[case] == 0:
                            del cases[case]
                            case_names.remove(case)
                    # count += 1
            # print(cases, days)
            case_to_check += 1
        if cases == {}:
                return days
            # if cases == {}:
            #     return days
                    
            # for case in case_names:
            #     if cases[case] == 0:
            #         del cases[case]
            #         case_names.remove(case)
        # print(cases, days)
        case_names = sorted([case for case in cases], key=lambda case: cases[case], reverse=True)
        
        daily_sessions = max_daily_sessions if max_daily_sessions < len(cases) else len(cases)

        days += 1
    # return days

    
        
    

if __name__ == "__main__":
    cases = {'A': 5, 'B': 7, 'C': 6, 'D': 11}
    max_daily_sessions = 2
    print(legal_backlog(cases, max_daily_sessions))

# start = {'A': 6, 'B': 3, 'C': 12, 'D': 14}
# 1 = {'A': 5, 'B': 3, 'C': 11, 'D': 13}
# 2 = {'A': 5, 'B': 3, 'C': 10, 'D': 12}
# 3 = {'A': 4, 'B': 3, 'C': 9, 'D': 11}
# 4 = {'A': 3, 'B': 3, 'C': 8, 'D': 10}
# 5 = {'A': 2, 'B': 3, 'C': 7, 'D': 9}
# 6 = {'A': 1, 'B': 3, 'C': 6, 'D': 8}
# 7 = {'B': 4,}
# 8 = {'B': 3,}
# 9 = {'B': 2,}
# 10 = {'B': 1,}
# 11 = {}