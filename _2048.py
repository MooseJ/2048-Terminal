import curses
from pieces import PIECES

_2048Map = {
    0: PIECES._blank,
    2: PIECES._2,
    4: PIECES._4,
    8: PIECES._8,
    16: PIECES._16,
    32: PIECES._32
}

_2048ColorMap = {
    0: 1,
    2: 2,
    4: 3,
    8: 4,
    16: 5,
    32: 6
}

class _2048:
    board = [] # 4 x 4 list
    def __init__(self):
        self.generateBoard()

    #TODO: clean up this disgusting mess
    #TODO: Also make displaying look better
    def displayBoard(self, stdscr):
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
                        piece = self.board[row][col]
                        stdscr.addstr(y, x, "*" if piece == 0 else str(piece), curses.color_pair(4))
    
    def betterDisplay(self, stdscr):
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
                currentPiece = self.board[row][col]
                drawing = _2048Map[currentPiece]
                color = _2048ColorMap[currentPiece]
                for i in range(x, x+12):
                    for j in range(y, y+5):
                        drawingCharacter = drawing[j-y][i-x]
                        try:
                            stdscr.addstr(j, i, drawingCharacter, curses.color_pair(color))
                        except curses.error:
                            pass
                x += 12
            y += 5
                

    def generateBoard(self):
        ## either use 0's for empty space or use constants for the piece names
        self.board = [
            [0,0,0,0],
            [4,4,8,0],
            [0,0,4,0],
            [4,0,0,0],
        ]
    
    #new algo
    #find spot to go to
    #if nothing found return

    #if empty spot, just go there.
    #otherwise merge
    def left(self):
        for col in range(4):
            for row in range (4):
                if(self.board[row][col] == 0):
                    continue
                nextColIndex = self.findNextCol(row, col, DIRECTION.LEFT)
                if(nextColIndex == -1):
                    continue
                
                if(self.board[row][nextColIndex] == 0):
                    self.board[row][nextColIndex] = self.board[row][col]
                    self.board[row][col] = 0
                else:
                    self.board[row][nextColIndex] *= 2
                    self.board[row][col] = 0
    
    def right(self):
        for col in range(3, -1, -1):
            for row in range (4):
                if(self.board[row][col] == 0):
                    continue
                nextColIndex = self.findNextCol(row, col, DIRECTION.RIGHT)
                if(nextColIndex == -1):
                    continue
                
                if(self.board[row][nextColIndex] == 0):
                    self.board[row][nextColIndex] = self.board[row][col]
                    self.board[row][col] = 0
                else:
                    self.board[row][nextColIndex] *= 2
                    self.board[row][col] = 0

    def up(self):
        for row in range(4):
            for col in range (4):
                if(self.board[row][col] == 0):
                    continue
                nextRowIndex = self.findNextRow(row, col, DIRECTION.UP)
                if(nextRowIndex == -1):
                    continue
                
                if(self.board[nextRowIndex][col] == 0):
                    self.board[nextRowIndex][col] = self.board[row][col]
                    self.board[row][col] = 0
                else:
                    self.board[nextRowIndex][col] *= 2
                    self.board[row][col] = 0
                    
    
    def down(self):
        for row in range(3, -1, -1):
            for col in range (4):
                if(self.board[row][col] == 0):
                    continue
                nextRowIndex = self.findNextRow(row, col, DIRECTION.DOWN)
                if(nextRowIndex == -1):
                    continue

                if(self.board[nextRowIndex][col] == 0):
                    self.board[nextRowIndex][col] = self.board[row][col]
                    self.board[row][col] = 0
                else:
                    self.board[nextRowIndex][col] *= 2
                    self.board[row][col] = 0

    def inBounds(self, row, col):
        return row >=0 and row <=3 and col >= 0 and col <=3

    def findNextCol(self, row, col, direction):
        currentValue = self.board[row][col]
        index = -1
        col += direction
        while(self.inBounds(row, col)):
            if(self.board[row][col] == currentValue):
                return col
            if(self.board[row][col] == 0):
                index = col
            col += direction
        return index
    
    def findNextRow(self, row, col, direction):
        currentValue = self.board[row][col]
        index = -1
        row += direction
        while(self.inBounds(row, col)):
            if(self.board[row][col] == currentValue):
                return row
            if(self.board[row][col] == 0):
                index = row
            row += direction
        return index

class DIRECTION:
    DOWN = 1
    UP = -1
    RIGHT = 1
    LEFT = -1