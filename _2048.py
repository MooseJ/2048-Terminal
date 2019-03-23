import curses

class _2048:
    board = [] # 4 x 4 list
    def __init__(self):
        self.generateBoard()

    #TODO: clean up this disgusting mess
    #TODO: Also make displaying look better
    def displayBoard(self, stdscr):
        for y in range(0, 9):
            if(y%2 == 0):
                stdscr.addstr(y,0, "."*9)
            else:
                for x in range (0, 9):
                    if(x%2 == 0):
                        stdscr.addstr(y, x, ".")
                    else:
                        col = x//2
                        row = y//2
                        piece = self.board[row][col]
                        stdscr.addstr(y, x, "*" if piece == 0 else str(piece))

    def generateBoard(self):
        ## either use 0's for empty space or use constants for the piece names
        self.board = [
            [0,0,0,0],
            [4,4,8,0],
            [0,0,4,0],
            [4,0,0,0],
        ]
    
    def left(self):
        for col in range(4):
            for row in range (4):
                if(self.board[row][col] == 0):
                    continue
                #find empty index
                emptyColIndex = self.findLeftEmptyColInRow(row, col)  
                if(emptyColIndex == -1):
                    if(col > 0 and self.canMerge(row, col, row, col-1)):
                        self.board[row][col-1] *=  2
                        self.board[row][col] = 0
                    continue
                #can you merge with the left spot
                if(self.canMerge(row, col, row, emptyColIndex-1)):
                    self.board[row][emptyColIndex-1] = self.board[row][col] * 2
                    self.board[row][col] = 0
                else:
                    #just move to the empty spot
                    self.board[row][emptyColIndex] = self.board[row][col]
                    self.board[row][col] = 0
    
    def right(self):
        for col in range(3, -1, -1):
            for row in range (4):
                if(self.board[row][col] == 0):
                    continue
                #find empty index
                emptyColIndex = self.findRightEmptyColInRow(row, col)  
                if(emptyColIndex == -1):
                    if(col < 3 and self.canMerge(row, col, row, col+1)):
                        self.board[row][col+1] *=  2
                        self.board[row][col] = 0
                    continue
                #can you merge with the left spot
                if(self.canMerge(row, col, row, emptyColIndex+1)):
                    self.board[row][emptyColIndex+1] = self.board[row][col] * 2
                    self.board[row][col] = 0
                else:
                    #just move to the empty spot
                    self.board[row][emptyColIndex] = self.board[row][col]
                    self.board[row][col] = 0
    
    def up(self):
        for row in range(4):
            for col in range (4):
                if(self.board[row][col] == 0):
                    continue
                #find empty index
                emptyRowIndex = self.findTopEmptyRowInCol(row, col)  
                if(emptyRowIndex == -1):
                    if(row > 0 and self.canMerge(row, col, row-1, col)):
                        self.board[row-1][col] *=  2
                        self.board[row][col] = 0
                    continue
                #can you merge with the left spot
                if(self.canMerge(row, col, emptyRowIndex-1, col)):
                    self.board[emptyRowIndex-1][col] = self.board[row][col] * 2
                    self.board[row][col] = 0
                else:
                    #just move to the empty spot
                    self.board[emptyRowIndex][col] = self.board[row][col]
                    self.board[row][col] = 0
    
    def down(self):
        for row in range(3, -1, -1):
            for col in range (4):
                if(self.board[row][col] == 0):
                    continue
                #find empty index
                emptyRowIndex = self.findBottomEmptyRowInCol(row, col)  
                if(emptyRowIndex == -1):
                    if(row <  3 and self.canMerge(row, col, row+1, col)):
                        self.board[row+1][col] *=  2
                        self.board[row][col] = 0
                    continue
                #can you merge with the left spot
                if(self.canMerge(row, col, emptyRowIndex+1, col)):
                    self.board[emptyRowIndex+1][col] = self.board[row][col] * 2
                    self.board[row][col] = 0
                else:
                    #just move to the empty spot
                    self.board[emptyRowIndex][col] = self.board[row][col]
                    self.board[row][col] = 0


    def findLeftEmptyColInRow(self, row, col):
        index = -1
        col -= 1
        while(col >= 0):
            if(self.board[row][col] == 0):
                index = col
            col -= 1
        return index

    def findRightEmptyColInRow(self, row, col):
        index = -1
        col += 1
        while(col <= 3):
            if(self.board[row][col] == 0):
                index = col
            col += 1
        return index
    
    def findTopEmptyRowInCol(self, row, col):
        index = -1
        row -= 1
        while(row >= 0):
            if(self.board[row][col] == 0):
                index = row
            row -= 1
        return index
    
    def findBottomEmptyRowInCol(self, row, col):
        index = -1
        row += 1
        while(row <= 3):
            if(self.board[row][col] == 0):
                index = row
            row += 1
        return index
    
    def canMerge(self, currentRow, currentCol, rowToMergeTo, colToMergeTo):
        return self.inBounds(rowToMergeTo, colToMergeTo) and self.board[rowToMergeTo][colToMergeTo] == self.board[currentRow][currentCol]

    def inBounds(self, row, col):
        return row >=0 and row <=3 and col > 0 and col <=3
