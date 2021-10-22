import os, curses
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
os.system("color")
def linear(words):# words must be a list of strings
    for _ in words:
         print(_)
         os.system("pause")
def choice(choices, choose_times=1):# choices must be a dict of string:list of strings
    for _ in range(choose_times):
        choice = input()
        if choice in choices:
            linear(choices[choice])
def looped_choice(choices, splash_string='\033[1;31;47mOBJECTION!\033[0;0m'):# choices must be a list of tuples(string, list of strings)
    i = 0
    while 1:
        print(choices[i][0])
        char = screen.getch()
        if char == curses.KEY_RIGHT:
            if i == len(choices):
                i = -1
            i += 1
        elif char == curses.KEY_LEFT:
            if i == 0:
                i = len(choices)
            i -= 1
        elif char == curses.KEY_ENTER:
            print(splash_string)
            linear(choices[i][2])
