# https://cs50.harvard.edu/python/2022/psets/2/camel/
# Implement a program that promts the user for camel case and the program outputs the corresponding name in snake case.

def main():
    camelCase = input("camelCase: ")

    if camelCase == "name":
        print("name")
    elif camelCase == "firstName":
        print("first_name")
    elif camelCase == "preferredFirstName":
        print("preferred_first_name")
main()




