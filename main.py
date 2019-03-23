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
        board.displayBoard(stdscr)

        if c == ord('q'):
            break  # Exit the while loop
        else:
            clearScreen(stdscr)
            board.displayBoard(stdscr)

    unInitCurses(stdscr)

def initCurses(stdscr):
    curses.noecho() #lets you see the keys you input??
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
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