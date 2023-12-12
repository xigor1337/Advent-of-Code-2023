"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

with open("input values.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]


def get_start(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "S":
                return (i, j)

    return (0, 0)


s_pos = get_start(lines)
current, last = None, s_pos

# Get next element after start
for d in [-1, 1]:
    y = s_pos[0] + d
    x = s_pos[1] + d

    if y < 0 or y > len(lines) or x < 0 or x > len(lines[0]):
        continue

    if lines[y][s_pos[1]] in ["|", "L", "J", "7", "F"]:  # TOP/BOTTOM
        current = (y, s_pos[1])
        break

    if lines[s_pos[0]][x] in ["-", "L", "J", "7", "F"]:  # LEFT/RIGHT
        current = (s_pos[0], x)
        break

suma = 1

# Run through loop
while current != s_pos:
    row, col = current
    item = lines[row][col]

    top, bottom = (row - 1, col), (row + 1, col)
    left, right = (row, col - 1), (row, col + 1)

    if item in ["|", "L", "J"] and row > 0 and lines[top[0]][top[1]] != "." and top != last:  # TOP
        current, last = top, current

    elif item in ["|", "F", "7"] and row < len(lines) and lines[bottom[0]][bottom[1]] != "." and bottom != last:  # BOTTOM
        current, last = bottom, current

    elif item in ["-", "7", "J"] and col > 0 and lines[left[0]][left[1]] != "." and left != last:  # LEFT
        current, last = left, current

    elif item in ["-", "F", "L"] and col < len(lines[0]) and lines[right[0]][right[1]] != "." and right != last:  # RIGHT
        current, last = right, current

    suma += 1

print(suma // 2)
