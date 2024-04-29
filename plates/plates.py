# https://cs50.harvard.edu/python/2022/psets/2/plates/


def main():
    plate = input("Plate: ")
    if is_valid_2(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid_1(s):
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        return True


def is_valid_2(s):
    lsplit = 0
    length = len(s)
    for letterchar in s:
        if letterchar.isalpha():
            lsplit += 1
    numbersplit = s[lsplit:length]
    if numbersplit.isdigit() and lsplit > 1:
        return True
    else:
        return False


# def is_valid_3(s):


# def is_valid_4(s):

# def is_valid_5(s):

# def is_valid_6(s):

# def is_valid_7(s):


main()
