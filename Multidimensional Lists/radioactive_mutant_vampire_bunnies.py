def bunnies_multiply(buns, mat, rws, cls):
    new_bunnies = set()
    for bun in buns:
        b_r, b_c = bun
        if b_r + 1 < rws:
            new_bunnies.add((b_r + 1, b_c))
            mat[b_r + 1][b_c] = 'B'
        if b_r - 1 >= 0:
            new_bunnies.add((b_r - 1, b_c))
            mat[b_r - 1][b_c] = 'B'
        if b_c + 1 < cls:
            new_bunnies.add((b_r, b_c + 1))
            mat[b_r][b_c + 1] = 'B'
        if b_c - 1 >= 0:
            new_bunnies.add((b_r, b_c - 1))
            mat[b_r][b_c - 1] = 'B'
    return new_bunnies, mat


rows, cols = [int(x) for x in input().split()]
p_r, p_c = 0, 0
bunnies = set()

matrix = []
for r in range(rows):
    matrix.append(list(input()))
    for c in range(cols):
        if matrix[r][c] == 'P':
            p_r = r
            p_c = c
        elif matrix[r][c] == 'B':
            bunnies.add((r, c))

matrix[p_r][p_c] = '.'
dir_mapper = {
    'U': lambda rw, cl: (rw - 1, cl),
    'D': lambda rw, cl: (rw + 1, cl),
    'L': lambda rw, cl: (rw, cl - 1),
    'R': lambda rw, cl: (rw, cl + 1)
}

commands = input()
won = True

for ch in commands:
    new_r, new_c = dir_mapper[ch](p_r, p_c)
    if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
        bunnies, matrix = bunnies_multiply(bunnies, matrix, rows, cols)
        break
    p_r, p_c = new_r, new_c
    bunnies, matrix = bunnies_multiply(bunnies, matrix, rows, cols)
    if matrix[new_r][new_c] == 'B':
        won = False
        break


[print(*row, sep='') for row in matrix]
if won:
    print(f"won: {p_r} {p_c}")
else:
    print(f"dead: {p_r} {p_c}")

