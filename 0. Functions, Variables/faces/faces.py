#Implementing a function called "convert" that accepts a str as input and returns the same input with any ":)" converted to 🙂.
# Also, any ":(" converted to 🙁)

def main():
    convert = input("Enter a sad or a happy emoji! ")

    convert = convert.replace(":)","🙂")
    convert = convert.replace(":(","🙁")

    print(convert)

main()
