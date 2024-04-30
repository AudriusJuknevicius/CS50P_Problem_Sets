# https://cs50.harvard.edu/python/2022/psets/3/fuel/



def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
            if y == 0:
                raise ZeroDivisionError("Denominator cannot be zero")
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


def convert(x, y):
    if x > y:
        return None
    else:
        answer1 = 100 / y
        answer2 = answer1 * x
        if answer2 <= 1:
            return 1
        elif answer2 >= 99:
              return 100
        else:
            return round(answer2)



main()
