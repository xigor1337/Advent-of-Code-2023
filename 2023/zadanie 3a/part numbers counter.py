#there is one mistake, sometimes it add thesame value twice, if there are two special symbols next to it
#answer is not correct

suma = 0

def visualization(line, index):
    lista = [[], [], []]
    index = index + 140

    lista[0].append(line[index - 140 - 3])
    lista[0].append(line[index - 140 - 2])
    lista[0].append(line[index - 140 - 1])
    lista[0].append(line[index - 140])
    lista[0].append(line[index - 140 + 1])
    lista[0].append(line[index - 140 + 2])
    lista[0].append(line[index - 140 + 3])

    lista[1].append(line[index - 1])
    lista[1].append(line[index - 2])
    lista[1].append(line[index - 3])
    lista[1].append(line[index])
    lista[1].append(line[index + 1])
    lista[1].append(line[index + 2])
    lista[1].append(line[index + 3])

    lista[2].append(line[index + 140 - 3])
    lista[2].append(line[index + 140 - 2])
    lista[2].append(line[index + 140 - 1])
    lista[2].append(line[index + 140])
    lista[2].append(line[index + 140 + 1])
    lista[2].append(line[index + 140 + 2])
    lista[2].append(line[index + 140 + 3])

    print("", lista[0], "\n",
          lista[1], "\n",
          lista[2])
    return lista

def check(lista):
    liczba1 = ""
    liczba2 = ""
    liczba3 = ""
    liczba3d = ""
    liczba4 = ""
    liczba4d = ""
    if lista[1][4].isdecimal(): #right
        if lista[1][5].isdecimal():
            if lista[1][6].isdecimal():
                liczba1 = lista[1][4] + lista[1][5] + lista[1][6]
            else:
                liczba1 = lista[1][4] + lista[1][5]
        else:
            liczba1 = lista[1][4]

    if lista[1][2].isdecimal(): #left
        if lista[1][1].isdecimal():
            if lista[1][0].isdecimal():
                liczba2 = lista[1][0] + lista[1][1] + lista[1][2]
            else:
                liczba2 = lista[1][1] + lista[1][2]
        else:
            liczba2 = lista[1][2]

    for i in range(5): #top 3
        if lista[0][i].isdecimal():
            if lista[0][i + 1].isdecimal():
                if lista[0][i + 2].isdecimal():
                    liczba3 = lista[0][i] + lista[0][i + 1] + lista[0][i + 2]
    if liczba3 == "":
        for i in range(1, 5): #top 2
            if lista[0][i].isdecimal():
                if lista[0][i + 1].isdecimal():
                    liczba3 = lista[0][i] + lista[0][i + 1]
        if liczba3 == "":
            for i in range(2, 5): #top 1
                if lista[0][i].isdecimal():
                        liczba3 = lista[0][i]
    if lista[0][2].isdecimal() and lista[0][3].isdecimal() == False and lista[0][4].isdecimal(): #double top
        for i in range(1):  # top 3
            if lista[0][i].isdecimal():
                if lista[0][i + 1].isdecimal():
                    if lista[0][i + 2].isdecimal():
                        liczba3d = lista[0][i] + lista[0][i + 1] + lista[0][i + 2]
        if liczba3d == "":
            for i in range(1, 5):  # top 2
                if lista[0][i].isdecimal():
                    if lista[0][i + 1].isdecimal():
                        liczba3d = lista[0][i] + lista[0][i + 1]
            if liczba3d == "":
                for i in range(2, 5):  # top 1
                    if lista[0][i].isdecimal():
                        liczba3d = lista[0][i]

    for i in range(5): #bottom 3
        if lista[2][i].isdecimal():
            if lista[2][i + 1].isdecimal():
                if lista[2][i + 2].isdecimal():
                    liczba4 = lista[2][i] + lista[2][i + 1] + lista[2][i + 2]
    if liczba4 == "":
        for i in range(1, 5): #bottom 2
            if lista[2][i].isdecimal():
                if lista[2][i + 1].isdecimal():
                    liczba4 = lista[2][i] + lista[2][i + 1]
        if liczba4 == "":
            for i in range(2, 5): #bottom 1
                if lista[2][i].isdecimal():
                        liczba4 = lista[2][i]
    if lista[2][2].isdecimal() and lista[2][3].isdecimal() == False and lista[2][4].isdecimal(): #double bottom
        for i in range(1):  # bottom 3
            if lista[2][i].isdecimal():
                if lista[2][i + 1].isdecimal():
                    if lista[2][i + 2].isdecimal():
                        liczba4d = lista[2][i] + lista[2][i + 1] + lista[2][i + 2]
        if liczba4d == "":
            for i in range(1, 5):  # bottom 2
                if lista[2][i].isdecimal():
                    if lista[2][i + 1].isdecimal():
                        liczba4d = lista[2][i] + lista[2][i + 1]
            if liczba4d == "":
                for i in range(2, 5):  # bottom 1
                    if lista[2][i].isdecimal():
                        liczba4d = lista[2][i]

    print(liczba1, liczba2, liczba3, liczba3d, liczba4, liczba4d)
    return liczba1, liczba2, liczba3, liczba3d, liczba4, liczba4d

with open("input values.txt", 'r') as file:
    lines = [file.readline().strip() for _ in range(3)]
    znaki = ['-', '&', '+', '$', '%', '#', '*', '@', '=', '/']
    while all(lines):
        print("Current set of three lines:", lines)
        line = ""
        for i in lines:
            line += i
        print(line, "\n") #consists of 3 lines
        for znak in znaki:
            index = -1
            while True:
                index = line[140:280].find(znak, index + 1)
                if index == -1:
                    break
                print(f"Found {znak} at index:", index + 140)
                liczby = check(visualization(line, index))
                print(liczby)
                for l in liczby:
                    if l != "":
                        suma += int(l)
                print(suma)
        lines.pop(0)
        next_line = file.readline().strip()
        lines.append(next_line)
print(suma)