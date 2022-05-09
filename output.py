import os
def printWinMessage():
    print('Congratulations! You Win!')

def printLosingMessage():
    print('You Lose!')

def printBoard(arr):
    os.system('cls')
    for i in range(4):
        print('|', end ="")
        for j in range(4):
            if arr[i][j]==0:
                print('    |', end = "")
            elif arr[i][j]//10==0:
                print('   ' + str(arr[i][j]) + '|', end = "")
            elif arr[i][j]//100==0:
                print('  ' + str(arr[i][j]) + '|', end = "")
            elif arr[i][j]//1000==0:
                print(' ' + str(arr[i][j]) + '|', end = "")
            else:
                print(str(arr[i][j]) + '|', end = "")
        print('\n')

def printSaveGameHelp():
    os.system('cls')
    print('e/E\t\texit game without saving it')
    print('s/S\t\tsave game')
    print('b/B\t\tback to game')
    print('> ', end = "")

def printNewGameHelp():
    os.system('cls')
    print('start new game? (y/n)')
    print('> ', end = "")

def saveGameToFile(arr):
    f = open("data.txt", "w")
    for i in range(4):
        for j in range(4):
            f.write(str(arr[i][j]))
            if i!=3 or j!=3:
                f.write("\n")
    f.close()
    print("saved to file")