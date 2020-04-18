from random import randint

def bot_one_turn(table):
    while True:
        x = randint(0, 2)
        y = randint(0, 2)

        if str(table[x][y]) not in "1-1":
            break

    update(x, y, 1, table)


def bot_two_turn(table):
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


for sla in range(30):
    table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    while True:
        bot_one_turn(table)
        teste = end_game_condition(table)
        if teste == 1:
            break
        elif teste == -1:
            break
        elif teste == 0:
            break

        bot_two_turn(table)
        teste = end_game_condition(table)
        if teste == 1:
            break
        elif teste == -1:
            break
        elif teste == 0:
            break

