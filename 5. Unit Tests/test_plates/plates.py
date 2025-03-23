def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    return is_valid_1(plate) and is_valid_2(plate) and is_valid_3(plate) and is_valid_4(plate)


def is_valid_1(s):
    return s[:2].isalpha()


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

def is_valid_4(s):
    if len(s) < 2 or len(s) > 6:
        return False
    return True


if __name__ == "__main__":
    main()
