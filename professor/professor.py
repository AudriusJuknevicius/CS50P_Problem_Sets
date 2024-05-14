# https://cs50.harvard.edu/python/2022/psets/4/professor/

import random


def main():
    ...


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level =! 1 or level =! 2 or level =! 3:
                return level
            raise ValueError("Wrong Value")




def generate_integer(level):
    if level == 1:
        A = randint(1, 9)
        B = randint(1, 9)
    elif level ==2:
        A = randint(10, 99)
        B = randint(10, 99)
    elif level ==3:
        A = randint(100, 999)
        B = randint(100, 999)



    level 1 = 1-9
    level 2 = 10-99
    level 3 = 100-999



if __name__ == "__main__":
    main()
