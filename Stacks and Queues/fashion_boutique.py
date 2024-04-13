clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())

racks_used = 0
while clothes_stack:
    racks_used += 1
    current_rack_capacity = rack_capacity
    while clothes_stack and clothes_stack[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes_stack.pop()

print(racks_used)
