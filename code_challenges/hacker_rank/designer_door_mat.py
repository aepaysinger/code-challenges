def draw_door_mat(size, greeting):
    height = int(size[0])
    length = int(size[1])
    greeting_design_count = int((length - int(len(greeting))) / 2)
    detail_a = ".|."
    detail_b = "-"
    result = []
    detail_b_count = int((length - 1) / 2)
    detail_a_count = 1

    if height % 2 == 0:
        return (
            "Mat size must be N * M . (N is an odd natural number, and M is 3 times N."
        )

    for n in range(int(height / 2)):
        result.append(
            (detail_b * (detail_b_count - 1))
            + (detail_a * detail_a_count)
            + (detail_b * (detail_b_count - 1))
        )
        detail_b_count -= 3
        detail_a_count += 2
    if len(greeting) % 2 == 0:
        result.append(
            (detail_b * (greeting_design_count + 1))
            + greeting
            + (detail_b * greeting_design_count)
        )
    else:
        result.append(
            (detail_b * greeting_design_count)
            + greeting
            + (detail_b * greeting_design_count)
        )

    detail_b_count = int(length / height)

    for n in range(int(height / 2)):
        result.append(
            (detail_b * (detail_b_count))
            + (detail_a * (detail_a_count - 2))
            + (detail_b * (detail_b_count))
        )
        detail_b_count += 3
        detail_a_count -= 2

    return "\n".join(result)


if __name__ == "__main__":
    size = ["7", "21"]
    greeting = "HOLA"
    print(draw_door_mat(size, greeting))
