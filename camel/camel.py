# https://cs50.harvard.edu/python/2022/psets/2/camel/
# Implement a program that promts the user for camel case and the program outputs the corresponding name in snake case.

def main():
    camelCase = finder(input("camelCase: "))

    def finder(fdr):
        for fdr.isupper() in fdr:
            return fdr



def main():
    camelCase = input("camelCase: ")

    names = finder(camelCase)
    names = finder(camelCase)
    print("names",sep="_")


    def finder(s):
        for char in s:
            if char.isupper():
                parts = s.split(char)
                return parts
            return [s]
