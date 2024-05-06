# https://cs50.harvard.edu/python/2022/psets/4/figlet/

import random
import sys
from pyfiglet import Figlet

figlet = Figlet()


def choice():
    if len(sys.argv) == 1:
        return choice1()
    elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
        return choice2()
    sys.exit("Too many or few arguments.")



def choice1():
    user_input = input("Input: ")
    figlet.setFont(font=random.choice(figlet.getFonts()))
    font_changed = figlet.renderText(user_input)

    print("Output: " + font_changed)

def choice2():
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        figlet.setFont(font=sys.argv[2])
        userinput2 = input("Input: ")
        final_font = figlet.renderText(userinput2)

        print("Output: " + final_font)

choice()






