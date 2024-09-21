
def main():
    fraction = input("Fraction: ")
    print(gauge)


def gauge(percentage):
    percentage = convert(percentage)
    if percentage >= 100:
        return("F")
    elif percentage <= 1:
        return("E")
    elif percentage == 100:
        return("F")
    else:
        return("{}%".format(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    else:
        answer1 = 100 / y
        percentage = answer1 * x
    return round(percentage)



if __name__ == "__main__":
    main()
