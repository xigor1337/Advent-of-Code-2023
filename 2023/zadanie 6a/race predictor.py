with open("input values.txt", 'r') as file:
    times = file.readline()
    distances = file.readline()
times = times.strip().split(" ")
times = [item for item in times if item]
print(times)
distances = distances.strip().split(" ")
distances = [item for item in distances if item]
print(distances)

winning = []
for time in times[1:]:
    possibilities = 0
    for speed in range(int(time) + 1):
        movement = speed * (int(time) - speed)
        if movement > int(distances[times.index(time)]):
            possibilities += 1
    winning.append(possibilities)
print("ways to win each race:", winning)
suma = 1
for i in winning:
    suma *= i
print(suma)