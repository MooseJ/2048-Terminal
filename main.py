import curses
from input_manager import InputManager
from _2048 import _2048

def main(stdscr):
    initCurses(stdscr)
    inputManager = InputManager(stdscr)
    board = _2048()
    
    while True:
        c = inputManager.GetInput()

        inputManager.HandleInput(c, board)
        clearScreen(stdscr)
        #board.debugDisplay(stdscr)
        board.display(stdscr)
        stdscr.refresh()
        #board.debugDisplay(stdscr)

        if c == ord('q'):
            break  # Exit the while loop
        # else:
        #     clearScreen(stdscr)q
        #     board.debugDisplay(stdscr)
        #     board.display(stdscr)

    unInitCurses(stdscr)

def initCurses(stdscr):
    curses.noecho() #lets you see the keys you input??
    curses.init_pair(1, curses.COLOR_BLACK, 251)
    curses.init_pair(2, curses.COLOR_BLACK, 255)
    curses.init_pair(3, curses.COLOR_BLACK, 228)
    curses.init_pair(4, curses.COLOR_BLACK, 221)
    curses.init_pair(5, curses.COLOR_BLACK, 215)
    curses.init_pair(6, curses.COLOR_BLACK, 209)
    curses.init_pair(7, curses.COLOR_BLACK, 196)
    curses.init_pair(8, curses.COLOR_BLACK, 160)
    curses.init_pair(9, curses.COLOR_BLACK, 227)
    curses.init_pair(10, curses.COLOR_BLACK, 220)
    curses.init_pair(11, curses.COLOR_BLACK, 214)
    curses.cbreak() #allows app to react to keys instantly without waiting for enter
    stdscr.keypad(True)

def unInitCurses(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def clearScreen(stdscr):
    stdscr.addstr(0, 0, "                        ")


if __name__ == "__main__":
    curses.wrapper(main)