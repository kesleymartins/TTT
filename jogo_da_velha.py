from random import randint

def show_table(jogadas):
    for x in range(len(jogadas)):
        for y in range(len(jogadas[x])):
            
            if jogadas[x][y] == 1:
                k = "X"
            elif jogadas[x][y] == 2:
                k = "O"
            else:
                k = " "

            print(f" {k} ", end="")

            if y != 2:
                print("|", end="")

        if x != 2:
            print("\n-----------")

    print("\n\n")


def condição_vitoria(jogadas):
    for v in range(0, 3):
        win_p, win_b = 0, 0

        for x in range(len(jogadas)):        
            if jogadas[x][v] == 1:
                win_p += 1
            elif jogadas[x][v] == 2:
                win_b += 1

            if win_p == 3:
                return 1
            elif win_b == 3:
                return -1

    for h in range(0, 3):
        win_p, win_b = 0, 0

        for x in range(len(jogadas)):        
            if jogadas[h][x] == 1:
                win_p += 1
            elif jogadas[h][x] == 2:
                win_b += 1

            if win_p == 3:
                return 1
            elif win_b == 3:
                return -1

    win_p, win_b = 0, 0
    for n in range(0, 3):
        if jogadas[n][n] == 1:
            win_p += 1
        elif jogadas[n][n] == 2:
            win_b += 1

        if win_p == 3:
            return 1
        elif win_b == 3:
            return -1

    win_p, win_b, x, y = 0, 0, 0, 2
    for n in range(0, 3):
        if jogadas[x][y] == 1:
            win_p += 1
        elif jogadas[x][y] == 2:
            win_b += 1

        x += 1
        y -= 1

        if win_p == 3:
            return 1
        elif win_b == 3:
            return -1

    cont = 0
    for x in range(0, 3):
        for y in range(0, 3):
            if jogadas[x][y] > 0:
                cont += 1

    if cont == 9:
        return -3

    return 0


def update_table(x, y, who, jogadas):
    del jogadas[x][y]
    jogadas[x].insert(y, who)


def player_turn(jogadas):
    while True:
        while True:
            x = str(input("Linha: "))

            if x in "123":
                break

        while True:
            y = str(input("Coluna: "))

            if y in "123":
                break

        if str(jogadas[int(x)-1][int(y)-1]) not in "12":
            break
        else:
            print("Jogada Inválida!")

    update_table(int(x)-1, int(y)-1, 1, jogadas)


def bot_turn(jogadas):    
    while True:
        x = randint(0, 2)
        y = randint(0, 2)

        if str(jogadas[x][y]) not in "12":
            break

    update_table(x, y, 2, jogadas)

jogadas = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

game_loop = True

while game_loop:    
    player_turn(jogadas)

    msg = 0

    if condição_vitoria(jogadas) == 1:
        msg = 1
        break
    elif condição_vitoria(jogadas) == -1:
        msg = 2
        break
    elif condição_vitoria(jogadas) == -3:
        msg = 3
        break
 
    bot_turn(jogadas)

    if condição_vitoria(jogadas) == 1:
        msg = 1
        break
    elif condição_vitoria(jogadas) == -1:
        msg = 2
        break
    elif condição_vitoria(jogadas) == -3:
        msg = 3
        break

    show_table(jogadas)


if msg == 1:
    print("\n====== Player wins!!! ======")
elif msg == 2:
    print("\n====== Bot wins!!! ======")
elif msg == 3:
    print("\n====== Empate!!! ======")

show_table(jogadas)