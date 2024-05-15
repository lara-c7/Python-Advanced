from collections import deque

cups_capacities = deque(int(x) for x in input().split())
bottles_capacities = deque(int(x) for x in input().split())
wasted_water = 0

while cups_capacities and bottles_capacities:
    while cups_capacities[0] > 0:
        current_bottle_capacity = bottles_capacities[-1]
        bottles_capacities[-1] -= cups_capacities[0]
        cups_capacities[0] -= current_bottle_capacity
        if bottles_capacities[-1] > 0:
            wasted_water += bottles_capacities[-1]
        bottles_capacities.pop()
        if cups_capacities[0] <= 0:
            cups_capacities.popleft()
            break

if not cups_capacities:
    print(f"Bottles: {' '.join(str(x) for x in bottles_capacities)}")
if not bottles_capacities:
    print(f"Cups: {' '.join(str(x) for x in cups_capacities)}")
print(f"Wasted litters of water: {wasted_water}")
