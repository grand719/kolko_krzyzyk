import random


field = []


def clearField():
    if len(field) == 9:
        for i in range(0, 9):
            field[i] = ' '
    else:
        for i in range(0, 9):
            field.append(' ')


def drawBoard(board):
    i = 0
    while i < len(board):
        print(board[i], "|", board[i+1], "|", board[i+2])
        i += 3


def playerMove(boardField):
    place = boardField - 1
    field[place] = 'x'


def aiMove(boardField):
    place = boardField - 1
    field[place] = 'o'


def isFull(number):
    number = number-1
    if field[number] == 'x' or field[number] == 'o':
        return True
    else:
        return False


def gameInit():
    while True:
        player = int(input('Podaj liczbe od 1-9'))
        if isFull(player):
            print('Pole jest zajete')
        elif ' ' not in field:
            print("Koniec gry")
            break
        else:
            playerMove(player)
            print('\n')
            drawBoard(field)
            break

    while True:
        ai = random.randrange(10)

        if ' ' not in field:
            print("Koniec gry")
            break
        elif isFull(ai):
            print('Pole jest zajete')
        else:
            aiMove(ai)
            print('\n')
            drawBoard(field)
            break


def winCheck():
    for i in range(0, 9, 3):
        if field[i] == 'x' and field[i+1] == 'x' and field[i+2] == 'x':
            return 'Player wins'
        elif field[i] == 'o' and field[i+1] == 'o' and field[i+2] == 'o':
            return 'Computer wins'
    for i in range(0, 3):
        if field[i] == 'x' and field[i+3] == 'x' and field[i+6] == 'x':
            return 'Player wins'
        elif field[i] == 'o' and field[i+3] == 'o' and field[i+6] == 'o':
            return 'Computer wins'
    if field[0] == 'x' and field[0+4] == 'x' and field[0+8] == 'x':
        return 'Player wins'
    elif field[0] == 'o' and field[0+4] == 'o' and field[0+8] == 'o':
        return 'Computer wins'
    if field[2] == 'x' and field[2+2] == 'x' and field[2+4] == 'x':
        return 'Player wins'
    elif field[2] == 'o' and field[2+2] == 'o' and field[2+4] == 'o':
        return 'Computer wins'


def startGame():
    drawBoard(field)
    while True:
        if winCheck() == 'Player wins':
            print("Gratulacje wygrałeś!!!")
            break
        elif winCheck() == 'Computer wins':
            print('Przegrałeś :(')
            break
        gameInit()


while True:
    nextGame = int(input('Gra z ai 1-tak 2-koniec'))
    if nextGame == 1:
        clearField()
        startGame()
    elif nextGame == 2:
        break
