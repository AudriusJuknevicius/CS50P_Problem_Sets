# https://cs50.harvard.edu/python/2022/psets/3/fuel/

try:
    x = 1
    y = int(input("Fraction: "))
except ValueError:
    print("Fraction is not an integer")
else:
    print(x/y)
