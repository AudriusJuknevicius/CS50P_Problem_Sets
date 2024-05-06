#https://cs50.harvard.edu/python/2022/psets/4/emojize/

import emoji

emoji_input = input("Input: ")
emoji_output = emoji.emojize(emoji_input)
print("Output: " + emoji_output)

