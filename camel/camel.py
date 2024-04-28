# https://cs50.harvard.edu/python/2022/psets/2/camel/
# Implement a program that promts the user for camel case and the program outputs the corresponding name in snake case.



def main():
    camelCase = input("camelCase: ")
    parts = finder(camelCase)

    if len(parts) <2:
        print("Snake Case:",camelCase)
    elif len(parts) >2:
        print("Snake Case:",parts)


def finder(s):
    for char in s:
        if char.isupper():
            parts = s.split(char)
            return parts
        break

main()
