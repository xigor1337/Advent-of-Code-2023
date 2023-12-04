#not finished

with open("input values.txt", 'r') as file:
    lines = [file.readline().strip() for _ in range(196)]
suma = 0
numer = 1
karty = [1]
for _ in range(195):
    karty.append(1)
line_number = 0
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
    for _ in range(karty[0 + line_number]):
        for i in winning:
            for j in numbers:
                if i == j:
                    matched += 1
    for i in range(matched):
        if line_number + i + 1 < len(karty):
            karty[line_number + i + 1] += 1
        else:
            pass
    print(line_number)
    line_number += 1
print(karty)
for i in karty:
    suma += i
print(suma)
