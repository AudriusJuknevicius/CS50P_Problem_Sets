def main():
    hello = input("Greeting: ").lower().strip()
    hello = value(hello)
    print(hello)


def value(greeting):
    if greeting.startswith("Hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"



if __name__ == "__main__":
    main()

def main():
    greeting = input("Greeting: ").lower().strip()

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


