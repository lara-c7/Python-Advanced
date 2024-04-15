from collections import deque

number_of_pumps = int(input())
start_position = 0
stops = 0
pumps_deque = deque()

for _ in range(number_of_pumps):
    current_petrol, distance = input().split()
    pumps_deque.append([int(current_petrol), int(distance)])

while stops < number_of_pumps:
    petrol = 0
    for i in range(number_of_pumps):
        petrol += pumps_deque[i][0]
        distance = pumps_deque[i][1]
        if petrol < distance:
            pumps_deque.rotate(-1)
            start_position += 1
            stops = 0
            break
        petrol -= distance
        stops += 1

print(start_position)
