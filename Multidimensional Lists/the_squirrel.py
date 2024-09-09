n_size = int(input())

s_row, s_col = 0, 0
hazelnuts = 0
directions = input().split(', ')

matrix = []
for row in range(n_size):
    curr_row = list(input())
    if 's' in curr_row:
        s_row = row
        s_col = curr_row.index('s')
    matrix.append(curr_row)

mapper = {'down': (1, 0),
          'up': (-1, 0),
          'right': (0, 1),
          'left': (0, -1)}

for direction in directions:
    s_row += mapper[direction][0]
    s_col += mapper[direction][1]
    if s_row < 0 or s_row >= n_size or s_col < 0 or s_col >= n_size:
        print("The squirrel is out of the field.")
        break
    elif matrix[s_row][s_col] == 'h':
        hazelnuts += 1
        matrix[s_row][s_col] = '*'
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break
    elif matrix[s_row][s_col] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        break
else:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")
