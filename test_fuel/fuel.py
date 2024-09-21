
def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
        except ValueError:
                print("Unexpected Input")
        else:
            answer = convert(x, y)
            if x == 100 and y == 100:
                print("F")
                break
            elif answer == 1:
                print("E")
                break
            elif answer == 100:
                print("F")
                break
            else:
                if answer != None:
                    print("{}%".format(answer))
                    break
                else:
                    print("Invalid fraction, please try again.")


def gauge(percentage):
    








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
