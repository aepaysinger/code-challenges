def what_time_is_it(angle):
    hour = int(angle//30)
    min = int((angle - (hour * 30)) * 2)
    if min < 10:
        min = "0" + str(min)
    if min == 0:
        min = "00"
    if hour < 10:
        hour = "0" + str(hour)
    if hour == "00":
        hour = 12
    return f"{hour}:{min}"



if __name__ == "__main__":
    angle = 193.266
    print(what_time_is_it(angle))