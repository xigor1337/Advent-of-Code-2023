import math

#for some reason somethimes it gose backwords, no idea why

with open("input values.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]

for line in lines:
    for i in line:
        if i == "S":
            s_line = lines.index(line)
            s_index = line.index(i)
print("location of S: line =", s_line, "index =", s_index)

grid = []
for i in range(len(lines)):
    grid.append([lines[i]])
for i in grid:
    print(i)

#| is a vertical pipe connecting north and south.
#- is a horizontal pipe connecting east and west.
#L is a 90-degree bend connecting north and east.
#J is a 90-degree bend connecting north and west.
#7 is a 90-degree bend connecting south and west.
#F is a 90-degree bend connecting south and east.
#. is ground; there is no pipe in this tile.
#S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

possibilities = {"|": "1",
                 "-": "1",
                 "L": "1",
                 "J": "1",
                 "7": "1",
                 "F": "1",}

current_index = s_index
current_line = s_line - 1
check = [current_index - 1, current_index + 1, current_line + 1, current_line - 1]
aaa = 0
suma = 0
last = ""
p = set()
ilosc = -1
while current_index != s_index or current_line != s_line:
    print("   " + lines[current_line - 1][current_index] + "\n", lines[current_line][current_index - 1], lines[current_line][current_index], lines[current_line][current_index + 1] + "\n", "  " + lines[current_line + 1][current_index ])
    check = [current_index - 1, current_index + 1, current_line + 1, current_line - 1, ""]
    check.remove(last)
    for e in check:
        if e == current_index + 1 and lines[current_line][current_index] != "|" and lines[current_line][current_index] != "7" and lines[current_line][current_index] != "J":
            if lines[current_line][current_index + 1] == "-" or lines[current_line][current_index + 1] == "J" or lines[current_line][current_index + 1] == "7":
                current_index += 1
                last = current_index - 1
                break
        if e == current_index - 1 and lines[current_line][current_index] != "|" and lines[current_line][current_index] != "L" and lines[current_line][current_index] != "F":
            if lines[current_line][current_index - 1] == "-" or lines[current_line][current_index - 1] == "L" or lines[current_line][current_index - 1] == "F":
                current_index -= 1
                last = current_index + 1
                break
        if e == current_line - 1 and lines[current_line][current_index] != "F" and lines[current_line][current_index] != "7" and lines[current_line][current_index] != "-":
            if lines[current_line - 1][current_index] == "|" or lines[current_line - 1][current_index] == "7" or lines[current_line - 1][current_index] == "F":
                current_line -= 1
                last = current_line + 1
                break
        if e == current_line + 1 and lines[current_line][current_index] != "L" and lines[current_line][current_index] != "J" and lines[current_line][current_index] != "-":
            if lines[current_line + 1][current_index] == "|" or lines[current_line + 1][current_index] == "J" or lines[current_line + 1][current_index] == "L":
                current_line += 1
                last = current_line - 1
                break
    print("\nlocation of ", lines[current_line][current_index], ": line =", current_line, "index =", current_index)
    suma += 1
    p.add(str(current_line) + " " + str(current_index))
    ilosc += 1
    if ilosc == len(p):
        aaa += 1
        if aaa == 1:
            print("blocked")
            break
print(suma)
print(math.sqrt(suma))