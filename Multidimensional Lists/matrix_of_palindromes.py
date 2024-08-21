r, c = [int(x) for x in input().split()]

start_letter = ord('a')

for row in range(r):
    for col in range(c):
        print(f'{chr(start_letter + row)}{chr(start_letter + row + col)}{chr(start_letter + row)}', end=' ')
    print()


# for row in range(r):
#     data = []
#     for col in range(c):
#         data.append(f"{chr(row + 97) + chr(row + col + 97) + chr(row + 97)}")
#     matrix.append(data)
#
# [print(*row) for row in matrix]
