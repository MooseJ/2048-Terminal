import curses

class InputManager:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def GetInput(self):
        return self.stdscr.getch()

    def HandleInput(self, key, board):
        if key == curses.KEY_UP:
            board.up()
        elif key == curses.KEY_DOWN:
            board.down()
        elif key == curses.KEY_LEFT:
            board.left()
        elif key == curses.KEY_RIGHT:
            board.right()
        return
