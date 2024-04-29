# https://cs50.harvard.edu/python/2022/psets/2/coke/
# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

def coke():
    cokebottle = 50

    while cokebottle !=0:
        inserted = int(input("Insert Coin: "))
        cokebottle = check(cokebottle)
        if cokebottle == 0:
            print("Change Owed: ",  cokebottle)
        else:
            print("Amount Due: ",  cokebottle)


def check(inserted, cokebottle):
    if inserted == 5 or inserted == 10 or inserted == 25:
        cokebottle -= inserted
    if cokebottle == 0:
        return 0
    else:
        return cokebottle

coke()
