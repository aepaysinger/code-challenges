from datetime import datetime


def get_gaurd_schedule():
    with open("code_challenges/advent_of_code/gaurd_schedule") as shifts:
        gaurd_schedule = shifts.read().split("\n")
    
    return [shift.replace("]", "").replace("[", "") for shift in gaurd_schedule]


def organize_schedule():
    schedule = get_gaurd_schedule()
    times_to_sort = []
    schedule = [[shift[0:16], shift[17:]] for shift in schedule]
    # print(schedule)
    # for time, action in schedule:
    #     times_to_sort.append(time[1:])
    # sorted_times = sorted(times_to_sort, key = lambda date: datetime.strptime(date, '%Y-%m-%d %H:%M'))
    # sorted_times = [[time] for time in sorted_times]
    # # for time, action in schedule:
    #     print(time, action)
    schedule = schedule.sort(key = lambda date, details: datetime.strptime((date, '%Y-%m-%d %H:%M'), details))
    # schedule = sorted(schedule, key = lambda date: datetime.strptime(date, '%Y-%m-%d %H:%M'))
    print(schedule)
    # return sorted_times

# print(get_gaurd_schedule())
print(organize_schedule())