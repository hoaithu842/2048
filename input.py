import output
import msvcrt
import os

def getSavedGame(arr):
    if os.path.exists("data.txt"):
        f = open("data.txt", "r")
        for i in range(4):
            for j in range(4):
                arr[i][j] = int(f.readline())
        f.close()
        os.remove("data.txt")

def getDirectionMove():
    #str = input('> ')
    str = msvcrt.getch()
    if str == b'a' or str == b'A':
        return 1
    elif str == b'd' or str == b'D':
        return 2
    elif str == b's' or str == b'S':
        return 3
    elif str == b'w' or str == b'W':
        return 4
    elif str == b'q' or str == b'Q':
        return 5
    elif str == b'n' or str == b'N':
        return 6
    else:
        return getDirectionMove()

def getSaveGameChoice():
    output.printSaveGameHelp()
    str = msvcrt.getch()
    if str == b'e' or str == b'E':
        return 1
    elif str == b's' or str == b'S':
        return 2
    elif str == b'b' or str == b'B':
        return 3
    else:
        return getSaveGameChoice()

def getNewGameChoice():
    output.printNewGameHelp()
    str = msvcrt.getch()
    if str == b'y' or str == b'Y':
        return 1
    elif str == b'n' or str == b'N':
        return 0
    else:
        return getNewGameChoice()