
def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def gauge(percentage):
    if percentage >= 100:
        return("F")
    elif percentage <= 1:
        return("E")
    else:
        return f"{percentage}%"


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    else:
        percentage = (x / y) * 100
    return round(percentage)



if __name__ == "__main__":
    main()
