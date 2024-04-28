# https://cs50.harvard.edu/python/2022/psets/1/interpreter/

# Interpreter is a program that prompts the user for an arithmetic expression and then calculates the output.

def main():
    x, y, z = input("Expression: ").split(" ")

    x = float(x)
    z = float(z)

    if y == "+":
        print(f"{x + z:.2}")
    elif y == "-":
        print(f"{x - z:.2}")
    elif y == "*":
        print(f"{x * z:.2}")
    elif y == "/":
        print(f"{x / z:.2}")


main()

