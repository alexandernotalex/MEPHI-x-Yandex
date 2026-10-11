def rotate(mat):
    if not isinstance(mat, list):
        raise TypeError("Matrix must be a list of lists")
    if len(mat) == 0:
        return []

    n = len(mat)
    for row in mat:
        if not isinstance(row, list):
            raise TypeError("Matrix must be a list of lists")
        if len(row) != n:
            raise ValueError("Matrix must be square")

    rotated = []
    for col in range(n):
        new_row = []
        for row in reversed(range(n)):
            new_row.append(mat[row][col])
        rotated.append(new_row)
    return rotated