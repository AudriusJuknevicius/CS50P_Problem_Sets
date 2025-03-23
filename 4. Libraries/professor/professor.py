# https://cs50.harvard.edu/python/2022/psets/4/professor/


import random


def main():
    A, B = get_level()
    score = 0
    loops = 0
    while loops < 10:
        wrongtimes = 0
        X = random.randint(A, B)
        Y = random.randint(A, B)
        answer = X + Y
        while wrongtimes != 3:
            try:
                useranswer = int(input(f"{X} + {Y} = "))
                if useranswer == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    wrongtimes += 1
            except ValueError:
                print("EEE")
                wrongtimes +=1
                pass
        loops += 1
        print(f"{X} + {Y} = ", answer)
    print("Score:", score)



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            A, B = generate_integer(level)
            if A != -1 and B != -1:
                return A, B

        except ValueError: ("Wrong Value")
        pass



def generate_integer(level):
    if level == 1:
        A = 0
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
    return -1, -1

if __name__ == "__main__":
    main()

