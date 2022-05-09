import input
import output
import process


arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
process.generateNewBlock(arr)
process.generateNewBlock(arr)
input.getSavedGame(arr)

while process.checkWin(arr)==-1:
    output.printBoard(arr)
    userChoice = process.update(arr)
    if userChoice == 1:
        process.generateNewBlock(arr)
    elif userChoice == -1:
        userChoice = input.getSaveGameChoice()
        if userChoice==1:
            exit()
        elif userChoice==2:
            output.saveGameToFile(arr)
            exit()
        elif userChoice==3:
            pass
    elif userChoice == -2:
        userChoice = input.getNewGameChoice()
        if userChoice==1:
            arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            process.generateNewBlock(arr)
            process.generateNewBlock(arr)
        elif userChoice==0:
            pass


if process.checkWin(arr)==1:
    output.printBoard(arr)
    output.printWinMessage()
else:
    output.printBoard(arr)
    output.printLosingMessage()