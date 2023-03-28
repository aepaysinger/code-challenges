import bisect


def sort_emotions(arr, order):
    happy_emotions = {(":D", 1), (":)", 2), (":|", 3), (":(", 4), ("T_T", 5)}
    sad_emotions = {(":D", 5), (":)", 4), (":|", 3), (":(", 2), ("T_T", 1)}
    if order:
        emotions = happy_emotions
    else:
        emotions = sad_emotions

    sorted_emotions = []

    for emotion in arr:
        current_emotion = [emotion, None]
        for emotion in emotions:
            if current_emotion[0] == emotion[0]:
                current_emotion[1] = emotion[1]
                if order:
                    bisect.insort_right(
                        sorted_emotions, current_emotion, key=lambda t: t[1]
                    )
                else:
                    bisect.insort_right(
                        sorted_emotions, current_emotion, key=lambda t: t[1]
                    )
    return [emotion[0] for emotion in sorted_emotions]


if __name__ == "__main__":
    arr = [":D", ":|", ":)", ":(", ":D"]
    order = True
    print(sort_emotions(arr, order))
