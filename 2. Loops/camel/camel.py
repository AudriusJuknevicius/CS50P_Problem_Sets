# https://cs50.harvard.edu/python/2022/psets/2/camel/
# Implement a program that promts the user for camel case and the program outputs the corresponding name in snake case.



def main():
    camelCase = input("camelCase: ")
    parts = finder(camelCase)

    if len(parts) < 2:
        print(camelCase)
    elif len(parts) > 1:
        snake_case = "_".join(parts).lower()
        print(snake_case)


def finder(s):
    parts = []
    current_part = ""

    for char in s:
        if char.isupper() and current_part:
            parts.append(current_part)
            current_part = char
        else:
            current_part += char

    if current_part:
        parts.append(current_part)

    return parts

main()
