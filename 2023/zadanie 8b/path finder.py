with open("input values.txt", 'r') as file:
    lines = [file.readline().strip() for _ in range(776)]
instructions = lines[0]
print(len(instructions), "instructions:", instructions)

path = {}
for i in lines[2:]:
    path[i.split(" ")[0]] = i.split(" ")[2][1:4], i.split(" ")[3][:3]
    #print(i.split(" ")[0], i.split(" ")[2][1:4], i.split(" ")[3][:3])
print("path:", path)

suma = 0
index = 0
droga = []
for i in path:
    if i[-1] == "A":
        droga.append(i)
print(droga)

#iteration for 1000 years
while True:
    check = index
    for j in droga:
        for i in path:
            if index == len(instructions):
                index = 0
            if j == i:
                if instructions[index] == "L" and index == check:
                    droga[droga.index(j)] = path[i][0]
                elif instructions[index] == "R" and index == check:
                    droga[droga.index(j)] = path[i][1]
    index += 1
    suma += 1
    udane = 0
    for i in droga:
        if i[-1] == "Z":
            udane += 1
    print(udane, droga)
    if udane == len(droga):
        break
print(droga)
print(suma)