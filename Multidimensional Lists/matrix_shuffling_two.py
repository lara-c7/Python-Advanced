def is_valid(l):
    if len(l) != 5 or l[0] != 'swap':
        return False
    try:
        first, second, third, last = map(int, l[1:])
        return 0 <= first < r and 0 <= second < c and 0 <= third < r and 0 <= last < c
    except ValueError:
        return False


r, c = [int(x) for x in input().split()]

matrix = [input().split() for row in range(r)]

command = input()
while command != 'END':
    line = command.split()
    if is_valid(line):
        num1r, num1c, num2r, num2c = map(int, line[1:])
        matrix[num1r][num1c], matrix[num2r][num2c] = matrix[num2r][num2c], matrix[num1r][num1c]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")
    command = input()

