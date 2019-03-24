import curses
import random
from pieces import PIECES

_2048Map = {
    0: PIECES._blank,
    2: PIECES._2,
    4: PIECES._4,
    8: PIECES._8,
    16: PIECES._16,
    32: PIECES._32,
    64: PIECES._64,
    128: PIECES._128,
    256: PIECES._256,
    512: PIECES._512,
    1024: PIECES._1024,
    2048: PIECES._2048
}

_2048ColorMap = {
    0: 1,
    2: 2,
    4: 3,
    8: 4,
    16: 5,
    32: 6,
    64: 7,
    128: 8,
    256: 9,
    512: 10,
    1024: 11,
    2048: 12
}

class _2048:
    def __init__(self):
        self.generateBoard()

    #TODO: clean up this disgusting mess
    #TODO: Also make displaying look better
    def debugDisplay(self, stdscr):
        for y in range(0, 9):
            if(y%2 == 0):
                stdscr.addstr(y,50, "."*9, curses.color_pair(4))
            else:
                for x in range (50, 59):
                    if(x%2 == 0):
                        stdscr.addstr(y, x, ".", curses.color_pair(4))
                    else:
                        col = (x-50)//2
                        row = y//2
                        piece = self.tiles[row][col]
                        stdscr.addstr(y, x, "*" if piece == 0 else str(piece), curses.color_pair(4))
    
    def display(self, stdscr):
        #start at x, y = 0,0, draw first piece in row, and then add 6 to x
        #then we move to the next row at x,y = 0, 5, and then add 6 to x
        # keep doing this until were out of pieces
        #need to convert x,y to position in board
        x = 0
        y = 0
        while(y < 20):
            x = 0
            while(x < 48):
                row = y//5
                col = x//12
                currentPiece = self.tiles[row][col]
                drawing = _2048Map[currentPiece]
                color = _2048ColorMap[currentPiece]
                for i in range(x, x+12):
                    for j in range(y, y+5):
                        drawingCharacter = drawing[j-y][i-x]
                        try:
                            stdscr.addstr(j, i, drawingCharacter + " ", curses.color_pair(color))
                        except curses.error:
                            pass

                x += 12
            y += 5
       
                

    def generateBoard(self):
        ## either use 0's for empty space or use constants for the piece names
        self.tiles = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
        self.generateTile()
        self.generateTile()
    
    def left(self):
        if(not self.isLeftMovePossible()):
            return
        for col in range(4):
            for row in range (4):
                if(self.tiles[row][col] == 0):
                    continue

                nextColIndex = self.findNextCol(row, col, DIRECTION.LEFT)    
                self.updateCol(row, col, nextColIndex)
        self.generateTile()
    
    def right(self):
        if(not self.isRightMovePossible()):
            return
        for col in range(3, -1, -1):
            for row in range (4):
                if(self.tiles[row][col] == 0):
                    continue

                nextColIndex = self.findNextCol(row, col, DIRECTION.RIGHT)
                self.updateCol(row, col, nextColIndex)
        self.generateTile()
    
    def updateCol(self, row, col, nextColIndex):
        if(nextColIndex == -1):
            return
        if(self.tiles[row][nextColIndex] == 0):
            self.tiles[row][nextColIndex] = self.tiles[row][col]
            self.tiles[row][col] = 0
        else:
            self.tiles[row][nextColIndex] *= 2
            self.tiles[row][col] = 0

    def up(self):
        if(not self.isUpMovePossible()):
            return
        for row in range(4):
            for col in range (4):
                if(self.tiles[row][col] == 0):
                    continue

                nextRowIndex = self.findNextRow(row, col, DIRECTION.UP)
                self.updateRow(row, col, nextRowIndex)
        self.generateTile()

    def down(self):
        if(not self.isDownMovePossible()):
            return
        for row in range(3, -1, -1):
            for col in range (4):
                if(self.tiles[row][col] == 0):
                    continue

                nextRowIndex = self.findNextRow(row, col, DIRECTION.DOWN)
                self.updateRow(row, col, nextRowIndex)
        self.generateTile()
    
    def updateRow(self, row, col, nextRowIndex):
        if(nextRowIndex == -1):
            return
        if(self.tiles[nextRowIndex][col] == 0):
            self.tiles[nextRowIndex][col] = self.tiles[row][col]
            self.tiles[row][col] = 0
        else:
            self.tiles[nextRowIndex][col] *= 2
            self.tiles[row][col] = 0

    def inBounds(self, row, col):
        return row >=0 and row <=3 and col >= 0 and col <=3

    def findNextCol(self, row, col, direction):
        currentValue = self.tiles[row][col]
        index = -1
        col += direction
        while(self.inBounds(row, col)):
            if(self.tiles[row][col] == currentValue):
                return col
            if(self.tiles[row][col] == 0):
                index = col
            col += direction
        return index
    
    def findNextRow(self, row, col, direction):
        currentValue = self.tiles[row][col]
        index = -1
        row += direction
        while(self.inBounds(row, col)):
            if self.tiles[row][col] == currentValue:
                return row
            if self.tiles[row][col] == 0:
                index = row
            row += direction
        return index

    def getEmptyPositions(self):
        emptyPositions = []
        for rowIndex, row in enumerate(self.tiles):
            for colIndex, tile in enumerate(row):
                if(tile == 0):
                    emptyPositions.append((rowIndex, colIndex))
        return emptyPositions
    
    def getScore(self):
        total = 0
        for row in self.tiles:
            for tile in row:
                total += tile
        return total
    
    def generateTile(self):
        empties = self.getEmptyPositions()
        randomNum = random.randint(0, len(empties))
        positionToGenerateAt = empties[randomNum%len(empties)]
        row = positionToGenerateAt[0]
        col = positionToGenerateAt[1]
        self.tiles[row][col] = 2
    
    def isDownMovePossible(self):
        for col in range (4):
            for row in range(2, -1, -1):
                if self.tiles[row][col] != 0 and (self.tiles[row+1][col] == 0
                or self.tiles[row][col] == self.tiles[row+1][col]):
                    return True
        return False

    def isUpMovePossible(self):
        for col in range (4):
            for row in range(1, 4):
                if self.tiles[row][col] != 0 and (self.tiles[row-1][col] == 0
                or self.tiles[row][col] == self.tiles[row-1][col]):
                    return True
        return False

    def isRightMovePossible(self):
        for row in range (4):
            for col in range(2, -1, -1):
                if self.tiles[row][col] != 0 and (self.tiles[row][col+1] == 0
                or self.tiles[row][col] == self.tiles[row][col+1]):
                    return True
        return False

    def isLeftMovePossible(self):
        for row in range (4):
            for col in range(1,4):
                if self.tiles[row][col] != 0 and (self.tiles[row][col-1] == 0
                or self.tiles[row][col] == self.tiles[row][col-1]):
                    return True
        return False



class DIRECTION:
    DOWN = 1
    UP = -1
    RIGHT = 1
    LEFT = -1