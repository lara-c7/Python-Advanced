n_size = int(input())
a_r, a_c = 0, 0

matrix = []
teabags = 0
out_or_down = False
for row in range(n_size):
    line = input().split()
    if 'A' in line:
        a_r = row
        a_c = line.index('A')
    matrix.append(line)

matrix[a_r][a_c] = '*'

mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    a_r += mapper[command][0]
    a_c += mapper[command][1]
    if a_r < 0 or a_r >= n_size or a_c < 0 or a_c >= n_size:
        out_or_down = True
        break
    elif matrix[a_r][a_c] == 'R':
        out_or_down = True
        matrix[a_r][a_c] = '*'
        break
    elif matrix[a_r][a_c].isdigit():
        teabags += int(matrix[a_r][a_c])
        matrix[a_r][a_c] = '*'
        if teabags >= 10:
            print("She did it! She went to the party.")
            break
    matrix[a_r][a_c] = '*'

if out_or_down:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]
