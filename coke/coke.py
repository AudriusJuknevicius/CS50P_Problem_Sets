# https://cs50.harvard.edu/python/2022/psets/2/coke/
# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

def coke():
    while  :
        inserted = int(input("Insert Coin: "))
        inserted = check(inserted)
        if inserted == 0:
            print("Change Owed: ",inserted)
            elif
            print("Amount Due: "),inserted



def check(inserted):
    cokebottle = 50
    if inserted = 5, 10, 25:
    cokebottle -= inserted
    if cokebottle == 0:
        return 0
    else:
        return cokebottle

coke()
