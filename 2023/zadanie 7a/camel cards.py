with open("input values.txt", 'r') as file:
    lines = [file.readline().strip() for _ in range(1000)]
five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

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
worth = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
worth = {"A": 13,
         "K": 12,
         "Q": 11,
         "J": 10,
         "T": 9,
         "9": 8,
         "8": 7,
         "7": 6,
         "6": 5,
         "5": 4,
         "4": 3,
         "3": 2,
         "2":1}

print(len(types), "types", types)
#jestem zmęczony ale można tu zrobić by sprawdzał kolejnościowo
for type in types:
    for i in range(len(type)):
        score = 0
        for j in range(i + 1, len(type)):
            for index in range(5):
                if worth[type[i][index]] < worth[type[j][index]]:
                    type[i], type[j] = type[j], type[i]
                    break