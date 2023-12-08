with open("input values.txt", 'r') as file:
    lines = [file.readline().strip() for _ in range(1000)]
five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

#nothing has change yet

def iteration_check(lenght, card):
    for i in range(len(card)):
        toak_check = 0
        for j in range(i, len(card)):
            if card[i] == card[j]:
                toak_check += 1
            if toak_check == lenght:
                return True
    return False

def uniqunes_check(length, card):
    seen_symbols = []
    for symbol in card:
        if symbol not in seen_symbols:
            seen_symbols.append(symbol)
    if len(seen_symbols) == length:
        return True
    else:
        return False

for line in lines:
    line_split = line.split(" ")
    card = line_split[0]
    bid = line_split[1]
    if card == len(card) * card[0]:
        five_of_a_kind.append(line)
    elif iteration_check(4, card) == True:
        four_of_a_kind.append(line)
    elif uniqunes_check(2, card) == True:
        full_house.append(line)
    elif iteration_check(3, card) == True:
        three_of_a_kind.append(line)
    elif uniqunes_check(3, card) == True:
        two_pair.append(line)
    elif iteration_check(2, card) == True:
        one_pair.append(line)
    else:
        high_card.append(line)
print(len(five_of_a_kind), "five_of_a_kind:", five_of_a_kind)
print(len(four_of_a_kind), "four_of_a_kind:", four_of_a_kind)
print(len(full_house), "full_house:", full_house)
print(len(three_of_a_kind), "three_of_a_kind:", three_of_a_kind)
print(len(two_pair), "two_pair:", two_pair)
print(len(one_pair), "one_pair:", one_pair)
print(len(high_card), "high_card:", high_card)

types = [five_of_a_kind, four_of_a_kind, full_house, three_of_a_kind, two_pair, one_pair, high_card]
worth1 = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
worth2 = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2":1}

print(len(types), "types", types)

for type in types:
    for _ in range(len(type)):
        for i in range(len(type) - 1):
            if type[i][0] != type[i + 1][0]:
                if worth2[type[i][0]] < worth2[type[i + 1][0]]:
                    type[i], type[i + 1] = type[i + 1], type[i]
            elif type[i][1] != type[i + 1][1]:
                if worth2[type[i][1]] < worth2[type[i + 1][1]]:
                    type[i], type[i + 1] = type[i + 1], type[i]
            elif type[i][2] != type[i + 1][2]:
                if worth2[type[i][2]] < worth2[type[i + 1][2]]:
                    type[i], type[i + 1] = type[i + 1], type[i]
            elif type[i][3] != type[i + 1][3]:
                if worth2[type[i][3]] < worth2[type[i + 1][3]]:
                    type[i], type[i + 1] = type[i + 1], type[i]
            elif type[i][4] != type[i + 1][4]:
                if worth2[type[i][4]] < worth2[type[i + 1][4]]:
                    type[i], type[i + 1] = type[i + 1], type[i]
            else:
                pass

print("sorted types", types)

multiplication = {}
for m in range(1000, 0, -1):
    multiplication[m] = 0
print(multiplication)

m = 1000
for type in types:
    for i in type:
        multiplication[m] = i.split(" ")[1]
        m -= 1
print(multiplication)

suma = 0
for i in multiplication:
    suma += int(i) * int(multiplication[i])
print(suma)