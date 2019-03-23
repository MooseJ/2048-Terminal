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
            # self.stdscr.addstr(0, 0, "Left Button Pressed",
            #   curses.color_pair(1))
        elif key == curses.KEY_RIGHT:
            board.right()
        self.stdscr.refresh()
        return
