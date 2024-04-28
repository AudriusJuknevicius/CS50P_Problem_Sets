# https://cs50.harvard.edu/python/2022/psets/2/camel/
# Implement a program that promts the user for camel case and the program outputs the corresponding name in snake case.



def main():
    camelCase = input("camelCase: ")
    parts = finder(camelCase)

    if len(parts) < 2:
        print("Snake Case:", camelCase)
    elif len(parts) > 1:
        print("Snake Case:", parts,sep="_")


def finder(s):
    parts = re.findall(r'[A-Z][^A-Z]*', s)
    return parts

main()
