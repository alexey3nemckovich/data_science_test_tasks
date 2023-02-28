def transpose_matrix(matrix):
    rows_count = len(matrix)
    if rows_count == 0:
        print("empty matrix won't be processed!")
        return

    cols_count = len(matrix[0])
    if cols_count == 0:
        print("empty matrix won't be processed!")
        return

    transposed_matrix = [[0] * rows_count for _ in range(cols_count)]

    for row in range(rows_count):
        for col in range(cols_count):
            transposed_matrix[col][row] = matrix[row][col]

    print(transposed_matrix)
    print(f"Source matrix dimensions = {rows_count}*{cols_count}.\nTransposed matrix dimensions = {cols_count}*{rows_count}.")


matrix_sample = [
    [1, 2, 3],
    [3, 4, 5]
]
transpose_matrix(matrix_sample)
