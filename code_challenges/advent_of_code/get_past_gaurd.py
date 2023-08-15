from datetime import datetime


def get_gaurd_schedule():
    with open("code_challenges/advent_of_code/gaurd_schedule") as shifts:
        gaurd_schedule = shifts.read().split("\n")

    return [shift.replace("]", "").replace("[", "") for shift in gaurd_schedule]


def organize_schedule():
    schedule = get_gaurd_schedule()
    schedule = [[shift[0:16], shift[17:]] for shift in schedule]
    schedule = sorted(
        schedule,
        key=lambda time_action: datetime.strptime(time_action[0], "%Y-%m-%d %H:%M"),
    )

    return schedule


def track_each_gaurd():
    gaurd_schedule = organize_schedule()
    gaurd_breakdown = {}
    gaurd = None

    for time, info in gaurd_schedule:
        time = time.split(" ")
        info = info.split(" ")
        if len(info) == 4:
            gaurd = info[1]
        if len(info) == 2:
            gaurd_breakdown[gaurd] = gaurd_breakdown.get(gaurd, []) + [int(time[1][3:])]
    return gaurd_breakdown


def find_gaurd_asleep_most():
    gaurd_breakdown = track_each_gaurd()
    gaurd = None
    longest_time_asleep = set()
    for gaurd, shift in gaurd_breakdown.items():
        i = 0
        j = 1
        total_time = 0
        for time in shift:
            if j > len(shift):
                break
            total_time += shift[j] - shift[i]
            i += 2
            j += 2
        longest_time_asleep.add((gaurd, total_time))
    gaurd_number, longest_sleep = None, 0
    for gaurd, time in longest_time_asleep:
        if time > longest_sleep:
            longest_sleep = time
            gaurd_number = gaurd

    return gaurd_number, longest_sleep


def when_to_sneak_in():
    gaurd_break_down = track_each_gaurd()
    gaurd, sleep_time = find_gaurd_asleep_most()
    minutes_asleep = {}

    i, j = 0, 1
    for _ in enumerate(gaurd_break_down[gaurd]):
        if j > len(gaurd_break_down[gaurd]):
            break
        for time in range(gaurd_break_down[gaurd][i], gaurd_break_down[gaurd][j]):
            minutes_asleep[time] = minutes_asleep.get(time, 0) + 1

        i += 2
        j += 2
    best_time, amount_time = 0, 0
    for minute, amount in minutes_asleep.items():
        if amount > amount_time:
            best_time = minute
            amount_time = amount

    return best_time * int(gaurd[1:])


def gaurd_who_sleeps_most_on_same_hour():
    gaurd_breakdown = track_each_gaurd()
    minutes_asleep = {}

    for gaurd, times in gaurd_breakdown.items():
        i, j = 0, 1
        minutes_asleep[gaurd] = {}
        for _ in range(len(times)):
            if j > len(gaurd_breakdown[gaurd]):
                break
            for time in range(gaurd_breakdown[gaurd][i], gaurd_breakdown[gaurd][j]):
                minutes_asleep[gaurd][time] = minutes_asleep[gaurd].get(time, 0) + 1

            i += 2
            j += 2
    gaurd_number, time, amount = None, 0, 0
    for gaurd, minutes in minutes_asleep.items():
        for minute, minute_amount in minutes.items():
            if minute_amount > amount:
                gaurd_number = gaurd
                time = minute
                amount = minute_amount

    return int(gaurd_number[1:]) * time
