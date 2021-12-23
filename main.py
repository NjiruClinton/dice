import random


# player selection
def player_1():
    input("Player 1:")
    player1()


def player_2():
    input("Player 2:")
    player2()


# players
def player1():

    s = [1, 2, 3, 4, 5, 6]

    x: int = random.choice(s)
    print(x)
    if x == 6:
        print("you won!!")
    else:
        player_2()


def player2():
    s = [1, 2, 3, 4, 5, 6]

    x: int = random.choice(s)
    print(x)
    if x == 6:
        print("you won!!")
    else:
        player_1()


player_1()
