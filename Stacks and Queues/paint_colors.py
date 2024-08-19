from collections import deque

all_colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
colors = []
main_colors = ['red', 'yellow', 'blue']
secondary_colors = {'orange': ('red', 'yellow'), 'purple': ('red', 'blue'), 'green': ('yellow', 'blue')}
substrings = deque(input().split())

while substrings:
    first_str = substrings.popleft()
    second_str = substrings.pop() if substrings else ''
    for col in (first_str + second_str, second_str + first_str):
        if col in main_colors or col in secondary_colors:
            colors.append(col)
            break
    else:
        if len(first_str) > 1:
            substrings.insert(len(substrings) // 2, first_str[:-1])
        if len(second_str) > 1:
            substrings.insert(len(substrings) // 2, second_str[:-1])


for color in colors:
    if color in secondary_colors.keys():
        sec_color1, sec_color2 = secondary_colors[color]
        if sec_color1 not in colors or sec_color2 not in colors:
            colors.remove(color)

print(colors)
