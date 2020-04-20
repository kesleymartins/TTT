from random import randint
import csv


def show_table(jogadas):
    for x in range(len(jogadas)):
        for y in range(len(jogadas[x])):
            
            if jogadas[x][y] == 1:
                k = "X"
            elif jogadas[x][y] == -1:
                k = "O"
            else:
                k = " "

            print(f" {k} ", end="")

            if y != 2:
                print("|", end="")

        if x != 2:
            print("\n-----------")

    print("\n\n")


def player_turn(table):
    while True:
        while True:
            x = str(input("Linha: "))

            if x in "123":
                break

        while True:
            y = str(input("Coluna: "))

            if y in "123":
                break

        if str(table[int(x)-1][int(y)-1]) not in "12":
            break
        else:
            print("Jogada Inválida!")

    update(int(x)-1, int(y)-1, 1, table)


def bot_turn(table):
    while True:
        x = randint(0, 2)
        y = randint(0, 2)

        if str(table[x][y]) not in "1-1":
            break

    update(x, y, -1, table)


def update(x, y, who, table):
    del table[x][y]
    table[x].insert(y, who)


def end_game_condition(table):
    diagonal_x = table[0][0]+ table[1][1] + table[2][2]
    diagonal_y = table[0][2]+ table[1][1] + table[2][0]

    cont = 0
    for x in range(3):
        cont += table[x].count(0)

        linha = table[x][0] + table[x][1] + table[x][2]
        coluna = table[0][x] + table[1][x] + table[2][x]

        if linha == 3 or coluna == 3 or diagonal_x == 3 or diagonal_y == 3:
            return 1
        elif linha == -3 or coluna == -3 or diagonal_x == -3 or diagonal_y == -3:
            return -1

    return cont


def make_csv_file(table, winner):
    lista = [[]]
    for x in range(3):
        for y in range(3):
            lista[0].append(str(table[x][y]))

    lista[0].append(str(winner))

    file = open('bot_x_bot.csv', 'a')
    with file:
        writer = csv.writer(file)
        
        for row in lista:
            writer.writerow(row)


def make_csv_file(table, winner):
    lista = [[]]
    for x in range(3):
        for y in range(3):
            lista[0].append(str(table[x][y]))

    lista[0].append(str(winner))

    file = open('player_x_bot.csv', 'a')
    with file:
        writer = csv.writer(file)
        
        for row in lista:
            writer.writerow(row)


table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

while True:
    player_turn(table)
    teste = end_game_condition(table)
    if teste == 1:
        break
    elif teste == -1:
        break
    elif teste == 0:
        break

    show_table(table)

    bot_turn(table)
    teste = end_game_condition(table)
    if teste == 1:
        break
    elif teste == -1:
        break
    elif teste == 0:
        break

    show_table(table)


make_csv_file(table, teste)

show_table(table)

if teste == 1:
    print("player")
elif teste == -1:
    print("bot")
elif teste == 0:
    print("Empate")