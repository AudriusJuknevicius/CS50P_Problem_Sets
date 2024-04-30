# https://cs50.harvard.edu/python/2022/psets/3/fuel/



def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
        except ValueError:
             print("Fraction is not an integer")
        else:
            break
        x = int(x)
        y = int(y)
        answer = 100 / y
        answer2 = answer * x
        print(str(answer2) + "%")
    # print(f"{answer*x}")
            # answer = (100 / y) * x
            # print(f"{answer}+"%"")

main()

# def main():
#     a = fuel()
#     print(a+"%")


# def fuel():
#     while True:
#          try:
#               return int(input("Fraction: ")).split("/")
#          except ValueError:

