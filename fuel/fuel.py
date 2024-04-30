# https://cs50.harvard.edu/python/2022/psets/3/fuel/



def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
        except ValueError:
             print("Fraction is not an integer")
        else:
            return
        print(f"{x + y}")
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

