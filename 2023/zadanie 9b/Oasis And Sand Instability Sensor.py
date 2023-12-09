with open("input values.txt", 'r') as file:
    lines = [file.readline().strip() for _ in range(200)]

suma = 0
for line in lines:
    line = line.split(" ")
    change = []
    change.append(line)
    print(change[0])
    for _ in range(len(change[0])):
        change.append([])
    for list in range(len(change)):
        for i in range(1, len(change[list])):
            value = change[list][i]
            last_value = change[list][i - 1]

            change[list + 1].append(int(value) - int(last_value))
        print(change[list + 1])
        if all([ v == 0 for v in change[list + 1]]):
            break
    for i in change:
        if not i:
            pass
        else:
            i.insert(0, 0)
    change = [ele for ele in change if ele != []]
    change[-2][0] = change[-2][1]
    for list in range(len(change) - 2, -1, -1):
        value = change[list][0]
        last_value = change[list - 1][1]

        change[list - 1][0] = int(last_value) - int(value)

        print(change[list])
    suma += change[0][0]
    print("-------------------------------------------")
print(suma)