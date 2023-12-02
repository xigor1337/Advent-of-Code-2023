values = open("input values.txt", "r")
suma = 0

#12 red cubes, 13 green cubes, and 14 blue cubes
red = 12
green = 13
blue = 14

for line in values:
    line = line.strip()
    line = line.split(";")
    games = []
    for i in line:
        games.append(i)
    games[0] = ""
    line = line[0].split(":")
    games[0] = line[1]
    line.pop()
    #print("games:", games)
    #print("line:", line)

    red_count = 0
    green_count = 0
    blue_count = 0
    for game in games:
        game = game.strip().split(",")
        #print("game: ", game)
        zbior_danych = {}
        for data in game:
            data = data.strip().split(" ")
            #print("data: ", data)
            zbior_danych[data[1]] = data[0]
        print("zbior_danych: ", zbior_danych)
        for data in zbior_danych:
            if data == "red":
                if int(zbior_danych[data]) > red_count:
                    red_count = int(zbior_danych[data])
            elif data == "blue":
                if int(zbior_danych[data]) > blue_count:
                    blue_count = int(zbior_danych[data])
            elif data == "green":
                if int(zbior_danych[data]) > green_count:
                    green_count = int(zbior_danych[data])
        print("red_count:", red_count, "\nblue_count:", blue_count, "\ngreen_count:", green_count)
    razem = red_count * blue_count * green_count
    suma += razem
    print(suma)
print(suma)
