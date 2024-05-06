# https://cs50.harvard.edu/python/2022/psets/4/adieu/

namelist = []

while True:
        try:
            userinput = input("Name: ")
            namelist.append(userinput)
        except EOFError:
            print("Adieu, adieu, to" + namelist)
            break

