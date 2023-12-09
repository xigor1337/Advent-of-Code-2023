from math import lcm
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

sumy = []
for i in droga:
    suma = 0
    index = 0
    current = i
    while current[-1] != "Z":
        if index == len(instructions):
            index = 0
        check = index
        for i in path:
            if index == len(instructions):
                index = 0
            if current == i:
                if instructions[index] == "L" and index == check:
                    current = path[i][0]
                    index += 1
                elif instructions[index] == "R" and index == check:
                    current = path[i][1]
                    index += 1
        suma += 1
    sumy.append(suma)
print(lcm(*sumy))