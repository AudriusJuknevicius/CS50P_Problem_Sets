# https://cs50.harvard.edu/python/2022/psets/4/professor/


import random


# def main():
    # T = 10
    # while T > 10:


    # T += 1



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            X, Y = generate_integer(level)
            print(X + Y)
            break
        except ValueError: ("Wrong Value")
        pass




def generate_integer(level):
    if level == 1:
        A = 1
        B = 9
        return A, B
    elif level == 2:
        A = 10
        B = 99
        return A, B
    elif level == 3:
        A = 100
        B = 999
        return A, B
    return False

get_level()

# if __name__ == "__main__":
#     main()



    # A = random.randint(100, 999)
    #     B = random.randint(100, 999)
    #     return A, B
