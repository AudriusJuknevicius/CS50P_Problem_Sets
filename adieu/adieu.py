# https://cs50.harvard.edu/python/2022/psets/4/adieu/


import inflect
p = inflect.engine()
namelist = []

while True:
        try:
            userinput = input("Name: ")
            namelist.append(userinput)
        except EOFError:
            if len(namelist) == 1:
                print("Adieu, adieu, to", namelist)

            elif len(namelist) ==2:
                names = p.join((namelist[0], namelist[1]))
                print("Adieu, adieu, to", names)
                elif

            break






mylist = p.join(("apple", "banana", "carrot"))
# "apple, banana, and carrot"

mylist = p.join(("apple", "banana"))
# "apple and banana"

mylist = p.join(("apple", "banana", "carrot"), final_sep="")
# "apple, banana and carrot"
