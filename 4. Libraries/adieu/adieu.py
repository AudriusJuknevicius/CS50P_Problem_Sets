# https://cs50.harvard.edu/python/2022/psets/4/adieu/


import inflect
p = inflect.engine()
namelist = []

while True:
        try:
            userinput = input("Name: ")
            namelist.append(userinput)
        except EOFError:
            if len(namelist) >= 1:
                namelist = p.join(namelist)
                print("Adieu, adieu, to", namelist)
                break

