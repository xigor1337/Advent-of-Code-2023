values = open("input values.txt", "r")
suma = 0
for line in values:
    number = ""
    line = line.strip()
    print(line)
    for znak in line:
        print(znak)
        if znak.isdecimal():
            number += znak
            print("number:", number)
            break
    for znak in range(len(line)):
        print(line[(len(line) - 1) - znak])
        if line[(len(line) - 1) - znak].isdecimal():
            number += line[(len(line) - 1) - znak]
            print("number:", number)
            break
    suma += int(number)
    print(suma)
print(suma)