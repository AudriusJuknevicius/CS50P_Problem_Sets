# https://cs50.harvard.edu/python/2022/psets/4/figlet/

import random
import sys
import figlet

figlet.getfonts()

#Check if any command-line arguments were provided.
if len(sys.argv) == 1:
    # if no command-line arguments, ask for input.
    user_input = input("Input: ")
    # Get a random font and render the input text using figlet.
    font_input = random.choice(figlet.getfonts())


    font_changed = figlet.rendertext(user_input, font_input)

    print("Output: " + font_changed)




# elif len(sys.argv) == 2:
#     ??????????????



# Checks that the provided command-line argument has first -f or --font or --font as the second. Otherwise exits.
# if sys.argv[1] != "-f" or sys.argv[1] != "--font" or sys.argv[2] != "--font":
#     sys.exit


# figlet = figlet(sys.argv)


# if len(sys.argv) == 0:
#     figlet.setFont(font=f)
#     sys.argv = random.choice(figlet.getFonts())
#     print(figlet.renderText(sys.argv))


# if len(sys.argv) == 0:
#     print(input("Input: ")




# user_input = input("Input: ")

# def random_figlet():

