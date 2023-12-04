with open("input values.txt", 'r') as file:
    lines = [file.readline().strip() for _ in range(196)]
suma = 0
for line in lines:
    line = line.split("|")
    print(line)
    numbers = line[1].split(" ")
    numbers = [item for item in numbers if item]
    print("numbers:", numbers)
    winning = line[0].split(":")
    winning = winning[1].split(" ")
    winning = [item for item in winning if item]
    print("winning:", winning)

    matched = 0
    for i in winning:
        for j in numbers:
            if i == j:
                if matched == 0:
                    matched += 1
                    print("matched first: ", i, j)
                else:
                    matched *= 2
                    print("matched another: ", i, j)
    suma += matched
print(suma)