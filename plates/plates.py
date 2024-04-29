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


# def is_valid_2(s):

# def is_valid_3(s):

# def is_valid_4(s):

# def is_valid_5(s):

# def is_valid_6(s):

# def is_valid_7(s):


main()
