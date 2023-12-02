values = open("input values.txt", "r")
suma = 0
words = {1: "one",
         2: "two",
         3: "three",
         4: "four",
         5: "five",
         6: "six",
         7: "seven",
         8: "eight",
         9: "nine"}
for line in values:
    number = ""
    line = line.strip()
    ile = 0
    line_copy = line
    line_copy2 = line
    for i in line:
        if len(line_copy) >= 3:
            slowo = ""
            for znak in range(0 + ile, 3 + ile):
                slowo += line[znak]
            for j in words:
                if words[j] == slowo:
                    number += str(j)
                    break
            if len(number) == 1:
                break

        if len(line_copy) >= 4:
            slowo = ""
            for znak in range(0 + ile, 4 + ile):
                slowo += line[znak]
            for j in words:
                if words[j] == slowo:
                    number += str(j)
                    break
            if len(number) == 1:
                break

        if len(line_copy) >= 5:
            slowo = ""
            for znak in range(0 + ile, 5 + ile):
                slowo += line[znak]
            for j in words:
                if words[j] == slowo:
                    number += str(j)
                    break
            if len(number) == 1:
                break

        if i.isdecimal():
            number += i
            break
        ile += 1
        line_copy = line_copy[1:]

    ile = 0
    for i in range(len(line)):
        if len(line_copy2) >= 3:
            slowo = ""
            for znak in range(2 + ile, -1 + ile, -1):
                slowo += line[((len(line) - 1) - znak)]
            for j in words:
                if words[j] == slowo:
                    number += str(j)
                    break
            if len(number) == 2:
                break
        if len(line_copy2) >= 4:
            slowo = ""
            for znak in range(3 + ile, -1 + ile, -1):
                slowo += line[((len(line) - 1) - znak)]
            for j in words:
                if words[j] == slowo:
                    number += str(j)
                    break
            if len(number) == 2:
                break

        if len(line_copy2) >= 5:
            slowo = ""
            for znak in range(4 + ile, -1 + ile, -1):
                slowo += line[((len(line) - 1) - znak)]
            for j in words:
                if words[j] == slowo:
                    number += str(j)
                    break
            if len(number) == 2:
                break

        if line[(len(line) - 1) - i].isdecimal():
            number += line[(len(line) - 1) - i]
            break
        ile += 1
        line_copy2 = line_copy2[1:]

    suma += int(number)

print(suma)