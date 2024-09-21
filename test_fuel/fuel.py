
def main():
    gauge

def gauge(percentage):
    percentage = convert(percentage)
    if percentage >= 100:
        print("F")
    elif percentage <= 1:
        print("E")
    elif percentage == 100:
        print("F")
    else:
        print("{}%".format(percentage))


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
        answer2 = answer1 * x
    return round(answer2)



if __name__ == "__main__":
    main()
