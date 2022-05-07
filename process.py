from random import randint
import input

def generateNewBlock(arr):
    while True:
        row = randint(0, 3)
        col = randint(0, 3)
        if arr[row][col]==0:
            arr[row][col] = 2
            break


def checkWin(arr):
    count = 0
    for i in range(4):
        for j in range(4):
            if arr[i][j]!=0:
                count = count + 1
            elif arr[i][j]==2048:
                return 1
    if count==16:
        return 0
    else:
        return -1


def pullLeft(arr):
    makeChange = 0

    for i in range(4):
        left = right = 0
        while left<4 and right<4:
            while left<4 and arr[i][left]==0:
                left = left + 1
            right = left+1
            while right<4 and arr[i][right]==0:
                right = right + 1
            if left<4 and right<4 and arr[i][left]==arr[i][right]:
                if makeChange==0:
                    makeChange = 1
                arr[i][left] = arr[i][left]*2
                arr[i][right] = 0
                left = right + 1
            else:
                left = right

        left = right = 0
        while left<4 and right<4:
            right = left
            while right<4 and arr[i][right]==0:
                right = right + 1
            if right<4:
                arr[i][left] = arr[i][right]
                if left!=right:
                    if makeChange==0:
                        makeChange = 1
                    arr[i][right] = 0
                left = left + 1
    
    return makeChange

def pullRight(arr):
    makeChange = 0

    for i in range(4):
        right = 3
        left  = 3
        while right>=0 and left>=0:
            while right>=0 and arr[i][right]==0:
                right = right - 1
            left = right-1
            while left>=0 and arr[i][left]==0:
                left = left - 1
            if right>=0 and left>=0 and arr[i][right]==arr[i][left]:
                if makeChange==0:
                    makeChange = 1
                arr[i][right] = arr[i][right]*2
                arr[i][left] = 0
                right = left - 1
            else:
                right = left

        right = 3
        left = 3
        while right>=0 and left>=0:
            left = right
            while left>=0 and arr[i][left]==0:
                left = left - 1
            if left>=0:
                arr[i][right] = arr[i][left]
                if right!=left:
                    if makeChange==0:
                        makeChange = 1
                    arr[i][left] = 0
                right = right - 1

    return makeChange

def pullDown(arr):
    makeChange = 0

    for i in range(4):
        down = 3
        up = 3
        while down>=0 and up>=0:
            while down>=0 and arr[down][i]==0:
                down = down - 1
            up = down-1
            while up>=0 and arr[up][i]==0:
                up = up - 1
            if down>=0 and up>=0 and arr[down][i]==arr[up][i]:
                if makeChange==0:
                    makeChange = 1
                arr[down][i] = arr[down][i]*2
                arr[up][i] = 0
                down = up - 1
            else:
                down = up

        down = 3
        up = 3
        while down>=0 and up>=0:
            up = down
            while up>=0 and arr[up][i]==0:
                up = up - 1
            if up>=0:
                arr[down][i] = arr[up][i]
                if down!=up:
                    if makeChange==0:
                        makeChange = 1
                    arr[up][i] = 0
                down = down - 1
        
    return makeChange

def pullUp(arr):
    makeChange = 0

    for i in range(4):
        up = 0
        down = 0
        while up<4 and down<4:
            while up<4 and arr[up][i]==0:
                up = up + 1
            down = up+1
            while down<4 and arr[down][i]==0:
                down = down + 1
            if up<4 and down<4 and arr[up][i]==arr[down][i]:
                if makeChange==0:
                    makeChange = 1
                arr[up][i] = arr[up][i]*2
                arr[down][i] = 0
                up = down + 1
            else:
                up = down

        up = 0
        down = 0
        while up<4 and down<4:
            down = up
            while down<4 and arr[down][i]==0:
                down = down + 1
            if down<4:
                arr[up][i] = arr[down][i]
                if up!=down:
                    if makeChange==0:
                        makeChange = 1
                    arr[down][i] = 0
                up = up + 1
                
    return makeChange

def update(arr):
    userChoice = input.getDirectionMove()
    if userChoice==1:
        return pullLeft(arr)
    elif userChoice==2:
        return pullRight(arr)
    elif userChoice==3:
        return pullDown(arr)
    elif userChoice==4:
        return pullUp(arr)
    elif userChoice==5:
        return -1
    elif userChoice==6:
        return -2
    else:
        return 0