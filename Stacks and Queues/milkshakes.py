from collections import deque

chocolate = deque([int(x) for x in input().split(', ')])
milk = deque([int(x) for x in input().split(', ')])

milk_shakes = 0

while milk and chocolate and milk_shakes < 5:
    last_choc = chocolate[-1]
    first_milk = milk[0]
    if last_choc <= 0 and first_milk <= 0:
        chocolate.pop()
        milk.popleft()
        continue
    if last_choc <= 0:
        chocolate.pop()
        continue
    if first_milk <= 0:
        milk.popleft()
        continue
    if last_choc == first_milk:
        milk_shakes += 1
        chocolate.pop()
        milk.popleft()
    else:
        milk.append(milk.popleft()) # or milk.rotate(-1)
        chocolate[-1] -= 5

if milk_shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(map(str, chocolate)) if chocolate else 'empty'}")
print(f"Milk: {', '.join(map(str, milk)) if milk else 'empty'}")
