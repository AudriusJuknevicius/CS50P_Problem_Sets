# https://cs50.harvard.edu/python/2022/psets/1/extensions/

#Output media type depending on the ending suffix for example cat.gif = image/gif.

def main():
    type = input("File name: ").lower().strip()

    match type:
        case type.endswith(".gif"):
            print("image/gif")
        case type.endswith(".jpg") | type.endswith(".jpeg"):
            print("image/jpeg")
        case type.endswith(".png"):
            print("image/png")
        case type.endswith(".pdf"):
            print("application/pdf")
        case type.endswith(".txt"):
            print("text/plain")
        case type.endswith(".zip"):
            print("application/zip")
        case _:
            print("application/octet-stream")


main()
