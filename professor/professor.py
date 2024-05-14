# https://cs50.harvard.edu/python/2022/psets/4/professor/

import random


def main():
    T = 10
    while T > 10:
        

    T += 1



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            X, Y = generate_integer(level)
            print(X + Y)

        except ValueError: ("Wrong Value")
        pass




def generate_integer(level):
    if level == 1:
        A = random.randint(1, 9)
        B = random.randint(1, 9)
        return A, B
    elif level == 2:
        A = random.randint(10, 99)
        B = random.randint(10, 99)
        return A, B
    elif level == 3:
        A = random.randint(100, 999)
        B = random.randint(100, 999)
        return A, B
    return False



if __name__ == "__main__":
    main()
