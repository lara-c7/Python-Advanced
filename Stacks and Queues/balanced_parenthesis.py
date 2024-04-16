from collections import deque

parenthesis_sequence = deque(input())
counter = 0
opening_brackets = '([{'
closing_brackets = ')]}'

while parenthesis_sequence and counter < len(parenthesis_sequence) / 2:
    if parenthesis_sequence[0] not in opening_brackets:
        break
    index = opening_brackets.index(parenthesis_sequence[0])
    if parenthesis_sequence[1] == closing_brackets[index]:
        parenthesis_sequence.popleft()
        parenthesis_sequence.popleft()
        parenthesis_sequence.rotate(counter)
        counter = 0
    else:
        parenthesis_sequence.rotate(-1)
        counter += 1

if parenthesis_sequence:
    print('NO')
else:
    print('YES')
