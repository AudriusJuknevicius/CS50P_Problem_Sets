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
    nsplit = 0
    for letterchar in s:
        if letterchar.isalpha():
            lsplit += 1
        else:
            
            nsplit += 1

    if lsplit > 1:
        return s[0:lsplit]


# def is_valid_3(s):

# def is_valid_4(s):

# def is_valid_5(s):

# def is_valid_6(s):

# def is_valid_7(s):


main()
