def rotate(matrix):
    rotated = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix) - 1, -1, -1):
            row.append(matrix[j][i])
        rotated.append(row)
    return rotated