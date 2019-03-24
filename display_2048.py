from game_2048 import Game2048
import curses
import constants.color_pairs as color_pairs
from pieces import TILES

_2048Map = {
    0: TILES._blank,
    2: TILES._2,
    4: TILES._4,
    8: TILES._8,
    16: TILES._16,
    32: TILES._32,
    64: TILES._64,
    128: TILES._128,
    256: TILES._256,
    512: TILES._512,
    1024: TILES._1024,
    2048: TILES._2048
}

_2048ColorMap = {
    0: color_pairs.COLOR_PAIR_BLANK,
    2: color_pairs.COLOR_PAIR_2,
    4: color_pairs.COLOR_PAIR_4,
    8: color_pairs.COLOR_PAIR_8,
    16: color_pairs.COLOR_PAIR_16,
    32: color_pairs.COLOR_PAIR_32,
    64: color_pairs.COLOR_PAIR_64,
    128: color_pairs.COLOR_PAIR_128,
    256: color_pairs.COLOR_PAIR_256,
    512: color_pairs.COLOR_PAIR_512,
    1024: color_pairs.COLOR_PAIR_1024,
    2048: color_pairs.COLOR_PAIR_2048
}

_titleText = '''
#### #### #  # ####
   # #  # #  # #  #
#### #  # #### ####
#    #  #    # #  #
#### ####    # ####
'''

_instructionsText = '''
How to Play
    1. Use the arrow keys to shift tiles to one side of the board
    2. If tiles collide with similar tiles, they will be merged, to create a number twice as large
    3. Create the 2048 tile to win

Press q to quit

Press n to start a new game
'''

_winText = "Congrats! You Won!"


_loseText = "No more possible moves available :("

def _scoreText(score):
    return "Current Score: " + str(score)

def _highScoreText(score):
    return "High Score: " + str(score)

class Display2048:
    def __init__(self):
        self._tile_width = 12
        self._tile_height = 5
        self._max_board_length = self._tile_height * 4
        self._max_board_width = self._tile_width * 4

        self._board_start_y = 8
        self._board_start_x = 8

    def display(self, stdscr, game2048: Game2048):
        self._drawTitle(stdscr)
        self._drawBoard(game2048, stdscr)
        self._drawInstructions(stdscr)
        self._drawScore(stdscr, game2048)
        self._drawWinOrLose(stdscr, game2048)
        

    def _drawWinOrLose(self, stdscr, game2048):
        message_start_x = self._board_start_x+self._max_board_width+5
        message_start_y = self._board_start_y+10

        if game2048.isWin():
            stdscr.addstr(message_start_y, message_start_x, _winText)
        elif game2048.isLoss():
            stdscr.addstr(message_start_y, message_start_x, _loseText)

    def _drawScore(self, stdscr, game2048):
        score_start_x = self._board_start_x+self._max_board_width+5
        score_start_y = self._board_start_y+5
        stdscr.addstr(score_start_y, score_start_x, _scoreText(game2048.getScore()))
        stdscr.addstr(score_start_y+2, score_start_x, _highScoreText(game2048.getHighScore()))

    def _drawInstructions(self, stdscr):
        instructions_start_y = self._board_start_y+self._max_board_length+2
        for index, line in enumerate(_instructionsText.splitlines()):
            stdscr.addstr(instructions_start_y+index, 10, line)

    def _drawTitle(self, stdscr):
        for index, line in enumerate(_titleText.splitlines()):
            stdscr.addstr(1+index, 25, line)

    # really need to make this cleaner
    def _drawBoard(self, game2048, stdscr):
        tiles = game2048.tiles
        y = self._board_start_y
        while((y-self._board_start_y) < self._max_board_length):
            x = self._board_start_x
            while((x-self._board_start_x) < self._max_board_width):
                current_tile_row = (y-self._board_start_y)//self._tile_height
                current_tile_column = (x-self._board_start_x)//self._tile_width
                current_tile = tiles[current_tile_row][current_tile_column]

                drawing = _2048Map[current_tile]
                color = _2048ColorMap[current_tile]

                for i in range(x, x+self._tile_width):
                    for j in range(y, y+self._tile_height):
                        drawingCharacter = drawing[j-y][i-x]
                        stdscr.addstr(j, i, drawingCharacter, curses.color_pair(color))

                x += self._tile_width
            y += self._tile_height
