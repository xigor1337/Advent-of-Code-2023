with open("input values.txt", 'r') as file:
    times = file.readline()
    distances = file.readline()
times = times.strip().split(" ")
times = [item for item in times if item]
print(times)
distances = distances.strip().split(" ")
distances = [item for item in distances if item]
print(distances)

times2 = ""
for i in times[1:]:
    times2 += i
distances2 = ""
for i in distances[1:]:
    distances2 += i
print(times2)
print(distances2)

possibilities = 0
for speed in range(int(times2) + 1):
    movement = speed * (int(times2) - speed)
    if movement > int(distances2):
        possibilities += 1

print(possibilities)