def rotate_matrix(matrix):
    rotated_matrix = []
    length = len(matrix)
    # for path in matrix:
    #     length += 1
    count = 0
    while count < (length * length):
        for path in reversed(matrix):
            rotated_matrix.append(path[0])
            del path[0]
            count += 1
    final_matrix = []
    start = 0
    stop = length * length
    step = length
    for i in range(start, stop, step):
        final_matrix.append(rotated_matrix[i:i+step])     

    return final_matrix  #"\n".join(map(str,final_matrix))


def rotate_v2(matrix):
    rotated = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix) - 1, -1, -1):
            row.append(matrix[j][i])
        rotated.append(row)
    return rotated


def rotate_v3(matrix):
    return [list(r) for r in zip(*matrix[::-1])]

if __name__ == "__main__":
    matrix = [
        [1,2,3,8],
        [4,5,6,8],
        [7,8,9,8],
        [9,8,7,6],
    ]
    print(rotate_matrix(matrix))