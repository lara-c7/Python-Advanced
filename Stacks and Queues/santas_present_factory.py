from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])
presents_points = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
made_presents_cnt = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}
presents_crafted = False

while materials and magic_levels:
    if materials[-1] == 0 and magic_levels[0] == 0:
        materials.pop()
        magic_levels.popleft()
        continue
    elif materials[-1] == 0:
        materials.pop()
        continue
    elif magic_levels[0] == 0:
        magic_levels.popleft()
        continue
    magic = materials[-1] * magic_levels[0]
    if magic in [150, 250, 300, 400]:
        made_presents_cnt[presents_points[magic]] += 1
        magic_levels.popleft()
        materials.pop()
    elif magic < 0:
        result = materials.pop() + magic_levels.popleft()
        materials.append(result)
    elif magic > 0:
        magic_levels.popleft()
        materials[-1] += 15

if made_presents_cnt['Doll'] > 0 and made_presents_cnt['Wooden train'] > 0:
    presents_crafted = True
if made_presents_cnt['Teddy bear'] > 0 and made_presents_cnt['Bicycle'] > 0:
    presents_crafted = True
print("The presents are crafted! Merry Christmas!" if presents_crafted else "No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")
for gift, count in sorted(made_presents_cnt.items()):
    if count:
        print(f"{gift}: {count}")
