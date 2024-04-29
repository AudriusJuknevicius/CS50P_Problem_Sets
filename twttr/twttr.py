# https://cs50.harvard.edu/python/2022/psets/2/twttr/
# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting
# vowels,much like Twitter was originally called twttr.

# In a file called twttr.py, implement a program that prompts the user for a str of text and
# then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.

def main():
    tweet = input("Input: ")
    tweet = change(tweet)
    print("Output: " + tweet)




def change(t):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    for character in t:
        if character in vowels:
            t = t.replace(vowels,"")
        return t
    else:
        return t

main()
