# https://cs50.harvard.edu/python/2022/psets/1/extensions/

#Output media type depending on the ending suffix for example cat.gif = image/gif.

def main():
    type = input("File name: ").lower().strip()

    match type:
        case type.endswith(".gif")
            print("image/gif")


