import curses
import random

class Game2048:
    def __init__(self):
        self.newGame()
        self._board_length = 4
        self._high_score = 0

    def newGame(self):
        self._generateBoard()
        self._score = 0

    def shiftLeft(self):
        self._shift(TRAVERSAL_DIRECTION.LEFT)
    
    def shiftRight(self):
        self._shift(TRAVERSAL_DIRECTION.RIGHT)

    def shiftUp(self):
        self._shift(TRAVERSAL_DIRECTION.UP)

    def shiftDown(self):
        self._shift(TRAVERSAL_DIRECTION.DOWN)

    def getScore(self):
        return self._score
    
    def getHighScore(self):
        return self._high_score
    
    def isLoss(self):
        return not self._isMovePossible(TRAVERSAL_DIRECTION.UP) and not self._isMovePossible(TRAVERSAL_DIRECTION.DOWN) \
               and not self._isMovePossible(TRAVERSAL_DIRECTION.LEFT) and not self._isMovePossible(TRAVERSAL_DIRECTION.RIGHT) 

    def isWin(self):
        for row in self.tiles:
            for tile in row:
                if tile == 2048:
                    return True
        return False

    def _generateBoard(self):
        self.tiles = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]

        self.tiles = [
            [2,4,8,16],
            [32,64,128,256],
            [512,1024,2048,0],
            [0,0,0,0],
        ]

        self._generateNewTile()
        self._generateNewTile()

    def _shift(self, direction):
        if(not self._isMovePossible(direction)):
            return
        traversal = self._generateTraversal(direction)
        for row, col in traversal:
            if(self.tiles[row][col] == 0):
                continue
            nextRow, nextCol = self._findNextTilePosition(row, col, direction)
            self._updateTile(row, col, nextRow, nextCol)
        self._generateNewTile()

    def _updateTile(self, row, col, nextRow, nextCol):
        if(nextRow == -1 or nextCol== -1):
            return
        if(self.tiles[nextRow][nextCol] == 0):
            self.tiles[nextRow][nextCol] = self.tiles[row][col]
            self.tiles[row][col] = 0
        else:
            self.tiles[nextRow][nextCol] *= 2
            self.tiles[row][col] = 0
            self._score += self.tiles[nextRow][nextCol]
            self._checkForNewHighScore()

    def _checkForNewHighScore(self):
        self._high_score = max(self._high_score, self._score)
    
    def _inBounds(self, row, col):
        return row >=0 and row < self._board_length and col >= 0 and col < self._board_length 

    # return -1, -1 if position to move to is not found
    def _findNextTilePosition(self, row, col, direction):
        currentValue = self.tiles[row][col]
        vector = DIRECTION_TO_VECTOR[direction]
        row += vector.rowVector
        col += vector.colVector
        
        nextPosition = (-1, -1)
        while(self._inBounds(row, col)):
            nextTileValue = self.tiles[row][col]
            #tile were checking is the same. Merge right away
            if nextTileValue == currentValue:
                return (row, col)
            #tile were checking has a completely different value. Return with the best position we found to move to, even if its -1,-1
            if nextTileValue != 0 and nextTileValue != currentValue:
                return nextPosition
            #tile were checking has a value of 0. mark this as the best weve seen so far
            if nextTileValue == 0:
                nextPosition = (row, col)
            row += vector.rowVector
            col += vector.colVector
        return nextPosition

    def _getEmptyPositions(self):
        emptyPositions = []
        for rowIndex, row in enumerate(self.tiles):
            for colIndex, tile in enumerate(row):
                if(tile == 0):
                    emptyPositions.append((rowIndex, colIndex))
        return emptyPositions
    
    def _generateNewTile(self):
        empties = self._getEmptyPositions()
        randomNum = random.randint(0, len(empties))
        positionToGenerateAt = empties[randomNum%len(empties)]
        row = positionToGenerateAt[0]
        col = positionToGenerateAt[1]
        self.tiles[row][col] = 2
    
    def _isMovePossible(self, direction):
        vector = DIRECTION_TO_VECTOR[direction]
        traversal = self._generateTraversal(direction)
        for row, col in traversal:
            nextRow = row + vector.rowVector
            nextCol = col + vector.colVector
            if not self._inBounds(nextRow, nextCol):
                continue

            currentTileValue = self.tiles[row][col]
            nextTileValue = self.tiles[row+vector.rowVector][col+vector.colVector]
            if currentTileValue != 0 and (nextTileValue == 0 or currentTileValue == nextTileValue):
                return True

        return False
    
    def _generateTraversal(self, direction):
        if direction == TRAVERSAL_DIRECTION.UP:
            return [(row, col) for row in range(4) for col in range(self._board_length)]
        elif direction == TRAVERSAL_DIRECTION.RIGHT:
            return [(row, col) for row in range(4) for col in range(self._board_length - 1, -1, -1)]
        elif direction == TRAVERSAL_DIRECTION.DOWN:
            return [(row, col) for col in range(4) for row in range(self._board_length - 1, -1, -1)]
        elif direction == TRAVERSAL_DIRECTION.LEFT:
            return [(row, col) for col in range(4) for row in range(self._board_length)]
        return []

class TRAVERSAL_DIRECTION:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Vector:
    def __init__(self, rowVector, colVector):
        self.rowVector = rowVector
        self.colVector = colVector

class GRID_VECTORS:
    UP = Vector(-1, 0)
    DOWN = Vector(1, 0)
    RIGHT = Vector(0, 1)
    LEFT = Vector(0, -1)

DIRECTION_TO_VECTOR = {
    TRAVERSAL_DIRECTION.UP: GRID_VECTORS.UP,
    TRAVERSAL_DIRECTION.DOWN: GRID_VECTORS.DOWN,
    TRAVERSAL_DIRECTION.RIGHT: GRID_VECTORS.RIGHT,
    TRAVERSAL_DIRECTION.LEFT: GRID_VECTORS.LEFT
}