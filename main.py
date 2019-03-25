import curses
from input_2048 import Input2048
from game_2048 import Game2048
from display_2048 import Display2048
from curses_setup import initCurses, unInitCurses

def main(stdscr):
    initCurses(stdscr)
    input2048 = Input2048(stdscr)
    game2048 = Game2048()
    display2048 = Display2048()

    while True:
        stdscr.clear()
        display2048.display(stdscr, game2048)
        keyPressed = input2048.GetInput()
        input2048.HandleInput(keyPressed, game2048)

        if keyPressed == ord('q'):
            break
        if keyPressed == ord('n'):
            game2048.newGame()

    unInitCurses(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)