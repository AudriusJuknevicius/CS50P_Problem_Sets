# https://cs50.harvard.edu/python/2022/psets/3/fuel/



def main():
    try:
        x, y = int(input("Fraction: ")).split("/")
    except ValueError:
             print("Fraction is not an integer")
    else:
          answer = (100 / y) * x
          print(answer+"%")



def main():
    a = fuel()
    print(a+"%")


def fuel():
    while True:
         try:
              return int(input("Fraction: ")).split("/")
         except ValueError:

