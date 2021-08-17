import pygame

WIDTH = 700
HEIGHT = 700

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

squareWidth = WIDTH//len(grid)
squareHeight = HEIGHT//len(grid)

done = False

orig_delay = 40
delay = orig_delay

grid[cellI][cellJ] = 2

grid[targetI][targetJ] = 3

def drawGrid(win):
    x = 0
    for i in range(len(grid)):
        y = 0
        for j in range(len(grid[i])):
            if [i, j] in used:
                pygame.draw.rect(win, (160, 32, 240), (x, y, squareWidth, squareHeight))
            if [i, j] in currentStack:
                pygame.draw.rect(win, (255, 255, 0), (x, y, squareWidth, squareHeight))
            if grid[i][j] == 1:
                pygame.draw.rect(win, (0, 0, 0), (x, y, squareWidth, squareHeight))
            if grid[i][j] == 2:
                pygame.draw.rect(win, (0, 255, 0), (x, y, squareWidth, squareHeight))
            if grid[i][j] == 3:
                pygame.draw.rect(win, (255, 0, 0), (x, y, squareWidth, squareHeight))
            if grid[i][j] == 0:
                pygame.draw.rect(win, (0, 0, 0), (x, y, squareWidth, squareHeight), 2)
            y += squareWidth
        x += squareHeight

def checkSides():
    global cellI, cellJ, done
    if (cellI, cellJ) == (9, 9):
        done = True
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
    global delay
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('')
    main = True
    while main:
        win.fill((255, 255, 255))
        drawGrid(win)
        delay -= 1
        if delay == 0:
            delay = orig_delay
            if done == False:
                checkSides()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False

        pygame.display.update()
    pygame.quit()
    
main()
