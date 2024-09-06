def move(size, rw, cl, direct, step, mapp, mat):
    desired_row = rw + mapp[direct][0] * step
    desired_col = cl + mapp[direct][1] * step
    if 0 <= desired_row < size and 0 <= desired_col < size and mat[desired_row][desired_col] == '.':
        return desired_row, desired_col
    return rw, cl


def shoot(size, rw, cl, direct, mapp, mat, tts, t_shot):
    while 0 <= rw < size and 0 <= cl < size:
        rw += mapp[direct][0]
        cl += mapp[direct][1]
        if 0 <= rw < size and 0 <= cl < size:
            if mat[rw][cl] == 'x':
                tts -= 1
                mat[rw][cl] = '.'
                t_shot.append([rw, cl])
                break
    return mat, tts, t_shot


n = 5
r, c = 0, 0
targets = 0
matrix = []


for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'A':
            r, c = row, col
        elif matrix[row][col] == 'x':
            targets += 1

targets_total = targets
targets_shot = []
mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
commands_num = int(input())
for _ in range(commands_num):
    command = input().split()
    action = command[0]
    if action == 'move':
        direction, steps = command[1], int(command[2])
        r, c = move(n, r, c, direction, steps, mapper, matrix)
    else:
        direction = command[1]
        matrix, targets, targets_shot = shoot(n, r, c, direction, mapper, matrix, targets, targets_shot)
        if targets == 0:
            print(f"Training completed! All {targets_total} targets hit.")
            break

if targets:
    print(f"Training not completed! {targets} targets left.")
[print(x) for x in targets_shot]
