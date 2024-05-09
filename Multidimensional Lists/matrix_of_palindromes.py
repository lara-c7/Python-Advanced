r, c = [int(x) for x in input().split()]

start_letter = ord('a')

for row in range(r):
    for col in range(c):
        print(f'{chr(start_letter + row)}{chr(start_letter + row + col)}{chr(start_letter + row)}', end=' ')
    print()
