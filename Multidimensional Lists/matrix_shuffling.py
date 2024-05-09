def coordinates_valid(row1, col1, row2, col2, r_, c_):
    return 0 <= row1 < r_ and 0 <= row2 < r_ and 0 <= col1 < c_ and 0 <= col2 < c_


r, c = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(r)]

while True:
    command = input()
    if command == "END":
        break
    lines = command.split()
    if lines[0] != 'swap' or len(lines) != 5:
        print("Invalid input!")
        continue
    r1, c1, r2, c2 = [int(x) for x in lines[1:]]
    if coordinates_valid(r1, c1, r2, c2, r, c):
        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")
