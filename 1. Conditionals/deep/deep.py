# https://cs50.harvard.edu/python/2022/psets/1/deep/

# Implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything.
#   Outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

    if answer == "42":
        print("Yes")
    elif answer == "forty-two":
        print("Yes")
    elif answer == "forty two":
        print("Yes")
    else: print("No")


main()
