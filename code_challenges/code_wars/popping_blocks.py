def pop_blocks(lst):
    updated_lst = []
    count = 0
    while count < len(lst):
        same = 1
        for i in range(len(lst) - 1):
            if lst[i] == lst[i + same]:
                try:
                    while lst[i] == lst[same + i]:
                        same += 1
                except IndexError:
                    return updated_lst[:i]

                updated_lst = lst[:i] + lst[i + same :]

                break
            count += 1
        if count == len(lst) - 1:
            return lst

        lst = updated_lst
        count = 0

    return updated_lst
