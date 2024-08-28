strings = input().split('|')
new = []
for i in range(len(strings) - 1, -1, -1):
    new.append(strings[i].split())
flattened = [i for row in new for i in row]
print(*flattened)
