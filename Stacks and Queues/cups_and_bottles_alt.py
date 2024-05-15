from collections import deque

cups_capacities = deque(int(x) for x in input().split())
bottles_capacities = deque(int(x) for x in input().split())
wasted_water = 0

while cups_capacities and bottles_capacities:
    current_cup = cups_capacities[0]
    while current_cup > 0:
        current_bottle = bottles_capacities.pop()
        current_cup -= current_bottle
    wasted_water -= current_cup
    cups_capacities.popleft()

if not cups_capacities:
    print(f"Bottles: {' '.join(str(x) for x in bottles_capacities)}")
if not bottles_capacities:
    print(f"Cups: {' '.join(str(x) for x in cups_capacities)}")
print(f"Wasted litters of water: {wasted_water}")
