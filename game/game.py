# https://cs50.harvard.edu/python/2022/psets/4/game/



import random

while True:
        try:
            chosenlevel = int(input("Level: "))
            if chosenlevel > 0:
                userlevel = chosenlevel * 10
                answer = random.choice(userlevel)



