def alter_matrix(idx_one, idx_two, mat, mappr):
    value = int(mat[idx_one][idx_two])
    mat[idx_one][idx_two] = 0
    for dir in mappr:
        r, c = dir
        desired_row = idx_one + r
        desired_col = idx_two + c
        if 0 <= desired_row < size and 0 <= desired_col < size:
            if mat[desired_row][desired_col] > 0:
                mat[desired_row][desired_col] -= value
    return mat


size = int(input())
total_sum = 0

matrix = []
for row in range(size):
    line = [int(x) for x in input().split()]
    matrix.append(line)

mapper = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

indexes_explode = input().split()
for index in indexes_explode:
    a, b = [int(x) for x in index.split(',')]
    if 0 <= a < size and 0 <= b < size:
        if matrix[a][b] > 0:
            matrix = alter_matrix(a, b, matrix, mapper)

alive_cells = 0
total_sum = 0
for row in range(size):
    for col in range(size):
        if matrix[row][col] > 0:
            total_sum += matrix[row][col]
            alive_cells += 1

print(f"Alive cells: {alive_cells}")
print(f"Sum: {total_sum}")
[print(*row) for row in matrix]
