# https://cs50.harvard.edu/python/2022/psets/1/extensions/

#Output media type depending on the ending suffix for example cat.gif = image/gif.

def main():
    ftype = input("File name: ").lower().strip()

    match ftype:
        case ftype(".gif"):
            print("image/gif")
        case ftype.endswith(".jpg") | ftype.endswith(".jpeg"):
            print("image/jpeg")
        case ftype.endswith(".png"):
            print("image/png")
        case ftype.endswith(".pdf"):
            print("application/pdf")
        case ftype.endswith(".txt"):
            print("text/plain")
        case ftype.endswith(".zip"):
            print("application/zip")
        case _:
            print("application/octet-stream")


main()
