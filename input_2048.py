import curses

class Input2048:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def GetInput(self):
        return self.stdscr.getch()

    def HandleInput(self, key, board):
        if key == curses.KEY_UP:
            board.shiftUp()
        elif key == curses.KEY_DOWN:
            board.shiftDown()
        elif key == curses.KEY_LEFT:
            board.shiftLeft()
        elif key == curses.KEY_RIGHT:
            board.shiftRight()
        return
