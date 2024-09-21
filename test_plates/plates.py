def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if is_valid_1(plate) and is_valid_2(plate) and is_valid_3(plate):
        return True
    else:
        return False


def is_valid_1(s):
    if s[:2].isalpha():
        if len(s) < 2 or len(s) > 6:
            return False
        else:
            return True
    else:
        return False



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



if __name__ == "__main__":
    main()
