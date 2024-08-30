def is_valid_knight(mvs, rw, cl, mat, cnt, knights_take):
    for mv in mvs:
        desired_row = rw + mv[0]
        desired_col = cl + mv[1]
        if 0 <= desired_row < len(mat) and 0 <= desired_col < len(mat):
            if mat[desired_row][desired_col] == 'K':
                cnt += 1
                knights_take = True
    return cnt, knights_take


n_size = int(input())

moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
knights = []

matrix = []
for r in range(n_size):
    matrix.append(list(input()))
    for c in range(n_size):
        if matrix[r][c] == 'K':
            knights.append((r, c))

removed_knights = 0

while True:
    knights_to_take = False
    max_num = 0
    max_knight = 0
    for knight in knights:
        counter = 0
        row, col = knight[0], knight[1]
        counter, knights_to_take = is_valid_knight(moves, row, col, matrix, counter, knights_to_take)
        if counter > max_num:
            max_num = counter
            max_knight = (row, col)
    if not knights_to_take:
        break
    knights.remove(max_knight)
    m_r, m_c = max_knight
    matrix[m_r][m_c] = '0'
    removed_knights += 1

print(removed_knights)
