# https://cs50.harvard.edu/python/2022/psets/4/figlet/

import random
import sys
import figlet


# Checks that the provided command-line argument has first -f or --font or --font as the second. Otherwise exits.
if sys.argv[1] != "-f" or sys.argv[1] != "--font" or sys.argv[2] != "--font":
    sys.exit


    

figlet = figlet(sys.argv)


if len(sys.argv) == 0:
    figlet.setFont(font=f)
    sys.argv = random.choice(figlet.getFonts())
    print(figlet.renderText(sys.argv))


# if len(sys.argv) == 0:
#     print(input("Input: ")




# user_input = input("Input: ")

# def random_figlet():

