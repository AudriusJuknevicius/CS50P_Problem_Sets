# https://cs50.harvard.edu/python/2022/psets/2/plates/


def main():
    plate = input("Plate: ")
    if is_valid_1(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid_1(s):
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        return True


def is_valid_2(s):
    split = 2
    for letters in s:
        if letters in s:






    def change(t):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    for character in t:
        if character in vowels:
            t = t.replace(character,"")
    return t

# def is_valid_3(s):

# def is_valid_4(s):

# def is_valid_5(s):

# def is_valid_6(s):

# def is_valid_7(s):


main()
