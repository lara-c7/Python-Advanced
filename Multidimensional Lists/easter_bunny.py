n_size = int(input())
b_r, b_c = 0, 0
positions = []

matrix = []
for row in range(n_size):
    matrix.append(input().split())
    for col in range(n_size):
        if matrix[row][col] == 'B':
            b_r, b_c = row, col

mapper = {
    'down': (1, 0),
    'up': (-1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

max_eggs = float('-inf')
direction_winner = ''

for dir in mapper:
    total_eggs = 0
    new_r, new_c = b_r, b_c
    positions_per_dir = []
    while True:
        new_r += mapper[dir][0]
        new_c += mapper[dir][1]
        if 0 <= new_r < n_size and 0 <= new_c < n_size:
            if matrix[new_r][new_c].isdigit():
                total_eggs += int(matrix[new_r][new_c])
                positions_per_dir.append([new_r, new_c])
            elif matrix[new_r][new_c] == 'X':
                break
        else:
            break
    if total_eggs > max_eggs and positions_per_dir:
        max_eggs = total_eggs
        direction_winner = dir
        positions = positions_per_dir


print(direction_winner)
[print(x, end='\n') for x in positions]
print(max_eggs)
