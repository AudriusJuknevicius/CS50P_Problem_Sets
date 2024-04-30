# https://cs50.harvard.edu/python/2022/psets/3/fuel/



def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
        except ValueError:
             print("Fraction is not an integer")
        else:
            break
    answer = convert(x, y)
    if answer == 1:
        print("E")
    elif answer == 100:
        print("F")
    else:
        print(answer, "%",sep="")


        # x = int(x)
        # y = int(y)
        # answer = 100 / y
        # answer2 = answer * x
    # print(f"{answer*x}")
            # answer = (100 / y) * x
            # print(f"{answer}+"%"")

def convert(x, y):
    x = int(x)
    y = int(y)
    answer1 = 100 / y
    answer2 = answer1 * x
    if answer2 <= 1:
        return 1
    elif answer2 >= 99:
        return 100
    else:
        return round(answer2)


main()

# def main():
#     a = fuel()
#     print(a+"%")


# def fuel():
#     while True:
#          try:
#               return int(input("Fraction: ")).split("/")
#          except ValueError:

