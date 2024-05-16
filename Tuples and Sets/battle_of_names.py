n_lines = int(input())
even_set = set()
odd_set = set()

for row in range(1, n_lines + 1):
    name_sum = sum([ord(char) for char in input()]) // row
    if name_sum % 2 == 0:
        even_set.add(name_sum)
    else:
        odd_set.add(name_sum)

if sum(even_set) == sum(odd_set):
    print(*odd_set.union(even_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')
