with open("input values.txt", 'r') as file:
    lines = [file.readline().strip() for _ in range(776)]
instructions = lines[0]
print("instructions:", instructions)

path = {}
for i in lines[2:]:
    path[i.split(" ")[0]] = i.split(" ")[2][1:4], i.split(" ")[3][:3]
    #print(i.split(" ")[0], i.split(" ")[2][1:4], i.split(" ")[3][:3])
print(path)
print(len(instructions))

suma = 0
index = 0
droga = "AAA"
while droga != "ZZZ":
    if index == len(instructions):
        index = 0
    check = index
    for i in path:
        if index == len(instructions):
            index = 0
        if droga == i:
            if instructions[index] == "L" and index == check:
                droga = path[i][0]
                index += 1
            elif instructions[index] == "R" and index == check:
                droga = path[i][1]
                index += 1
    suma += 1
    print(droga)
print(droga)
print(suma)