
def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError) as e:
        print(e)


def gauge(percentage):
    if percentage >= 99:
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
        raise ValueError("X was higher than Y")
    elif y == 0:
        raise ZeroDivisionError("Y cannot be zero")
    else:
        percentage = (x / y) * 100
    return round(percentage)



if __name__ == "__main__":
    main()
