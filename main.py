grid = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]

used = []
currentStack = []

cellI, cellJ = 0, 0

targetI, targetJ = 9, 9

grid[cellI][cellJ] = 2

grid[targetI][targetJ] = 3

def drawGrid():
    for i in range(len(grid)):
        final = ""
        for j in range(len(grid[i])):
            final += str(grid[i][j])
        print(final)

def checkSides():
    global cellI, cellJ
    if (cellI, cellJ) == (9, 9):
        return "done"
    if cellI < len(grid) - 1 and grid[cellI + 1][cellJ] != 1 and [cellI + 1, cellJ] not in used:
        grid[cellI][cellJ] = 0
        cellI += 1
        grid[cellI][cellJ] = 2
    elif cellI > 0 and grid[cellI - 1][cellJ] != 1 and [cellI - 1, cellJ] not in used:
        grid[cellI][cellJ] = 0
        cellI -= 1
        grid[cellI][cellJ] = 2
    elif cellJ < len(grid[0]) - 1 and grid[cellI][cellJ + 1] != 1 and [cellI, cellJ + 1] not in used:
        grid[cellI][cellJ] = 0
        cellJ += 1
        grid[cellI][cellJ] = 2
    elif cellJ > 0 and grid[cellI][cellJ - 1] != 1 and [cellI, cellJ - 1] not in used:
        grid[cellI][cellJ] = 0
        cellJ -= 1
        grid[cellI][cellJ] = 2
    else:
        grid[cellI][cellJ] = 0
        cellI, cellJ = currentStack[-2][0], currentStack[-2][1]
        grid[cellI][cellJ] = 2
        currentStack.pop()
        return
    currentStack.append([cellI, cellJ])
    used.append([cellI, cellJ])

def main():
    while True:
        drawGrid()
        print()
        if checkSides() == "done":
            print("done")
            break
main()
