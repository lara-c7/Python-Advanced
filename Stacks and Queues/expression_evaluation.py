from collections import deque
from math import floor

expression = input().split()
numbers = deque()

for ch in expression:
    if ch.lstrip('-').isdigit():
        numbers.append(int(ch))
    elif ch in '+-*/':
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()
            if ch == '+':
                numbers.appendleft(first_number + second_number)
            elif ch == '-':
                numbers.appendleft(first_number - second_number)
            elif ch == '*':
                numbers.appendleft(first_number * second_number)
            elif ch == '/':
                numbers.appendleft(floor(first_number / second_number))

print(*numbers)
