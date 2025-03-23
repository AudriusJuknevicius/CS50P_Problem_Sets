# https://cs50.harvard.edu/python/2022/psets/2/plates/


def main():
    plate = input("Plate: ")
    if is_valid_1(plate) and is_valid_2(plate) and is_valid_3(plate):
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
    number0check = s[lsplit:lsplit + 1]
    if lsplit == length:
        return True
    elif numbersplit.isdigit() and lsplit > 1 and number0check != "0":
        return True
    else:
        return False


def is_valid_3(s):
    return s.isalnum()


main()
