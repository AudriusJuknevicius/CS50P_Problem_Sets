# https://cs50.harvard.edu/python/2022/psets/4/game/



import random

while True:
            try:
                chosenlevel = int(input("Level: "))
                if chosenlevel > 0:
                    answer = random.randint(1, chosenlevel)

                    while True:
                        guess = int(input("Guess: "))

                        if guess > 0:
                            if guess > answer:
                                print("Too large!")

                            elif guess < answer:
                                print("Too small!")

                            elif guess == answer:
                                print("Just right!")
                                break

                        else:
                            print("Invalid Guess")

                    break

                else:
                    print("Invalid Level")
            except ValueError:
                 pass






