# https://cs50.harvard.edu/python/2022/psets/4/professor/

import random


def main():
    ...


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            
                return level




def generate_integer(level):
    if level == 1:
        A = random.randint(1, 9)
        B = random.randint(1, 9)
        return A, B
    elif level ==2:
        A = random.randint(10, 99)
        B = random.randint(10, 99)
        return A, B
    elif level ==3:
        A = random.randint(100, 999)
        B = random.randint(100, 999)
        return A, B
    else:
        raise ValueError("Wrong Value")



    level 1 = 1-9
    level 2 = 10-99
    level 3 = 100-999



if __name__ == "__main__":
    main()
