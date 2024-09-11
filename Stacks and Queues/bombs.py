from collections import deque

bomb_effects = deque([int(x) for x in input().split(',')])
bomb_casings = [int(x) for x in input().split(',')]
done = False

bombs_values = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}
bombs_made = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
while bomb_effects and bomb_casings:
    total_sum = bomb_effects[0] + bomb_casings[-1]
    if total_sum in bombs_values.keys():
        bombs_made[bombs_values[total_sum]] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5
    for num in bombs_made.values():
        if num != 3:
            break
    else:
        done = True
        break

if done:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")
for bomb, cnt in sorted(bombs_made.items()):
    print(f"{bomb}: {cnt}")
