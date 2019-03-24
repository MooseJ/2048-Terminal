import curses
import constants.colors_256 as colors_256
import constants.color_pairs as color_pairs

def initCurses(stdscr):
    curses.noecho()
    curses.curs_set(0)
    initCurseColors()
    curses.cbreak()
    stdscr.keypad(True)

def unInitCurses(stdscr):
    curses.nocbreak()
    curses.curs_set(1)
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def initCurseColors():
    curses.init_pair(color_pairs.COLOR_PAIR_BLANK, curses.COLOR_BLACK, colors_256.GREY_70)
    curses.init_pair(color_pairs.COLOR_PAIR_2, curses.COLOR_BLACK, colors_256.GREY_93)
    curses.init_pair(color_pairs.COLOR_PAIR_4, curses.COLOR_BLACK, colors_256.CORN_SILK_1)
    curses.init_pair(color_pairs.COLOR_PAIR_8, curses.COLOR_BLACK, colors_256.LIGHT_GOLDEN_ROD_2)
    curses.init_pair(color_pairs.COLOR_PAIR_16, curses.COLOR_BLACK, colors_256.SANDY_BROWN)
    curses.init_pair(color_pairs.COLOR_PAIR_32, curses.COLOR_BLACK, colors_256.LIGHT_SALMON_1)
    curses.init_pair(color_pairs.COLOR_PAIR_64, curses.COLOR_BLACK, colors_256.SALMON_1)
    curses.init_pair(color_pairs.COLOR_PAIR_128, curses.COLOR_BLACK, colors_256.KHAKI_1)
    curses.init_pair(color_pairs.COLOR_PAIR_256, curses.COLOR_BLACK, colors_256.LIGHT_GOLDEN_ROD_1)
    curses.init_pair(color_pairs.COLOR_PAIR_512, curses.COLOR_BLACK, colors_256.LIGHT_GOLDEN_ROD_3)
    curses.init_pair(color_pairs.COLOR_PAIR_1024, curses.COLOR_BLACK, colors_256.GOLDEN_1)
    curses.init_pair(color_pairs.COLOR_PAIR_2048, curses.COLOR_BLACK, colors_256.ORANGE_1)

