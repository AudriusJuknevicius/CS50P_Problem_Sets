# https://cs50.harvard.edu/python/2022/psets/1/extensions/

#Output media type depending on the ending suffix for example cat.gif = image/gif.

def main():
    ftype = input("File name: ").lower().strip()

    if ".gif" in ftype:
        print("image/gif")
    elif ".jpg" in ftype or "jpeg" in ftype:
        print("image/jpeg")
    elif ".png" in ftype:
        print("image/png")
    elif ".pdf" in ftype:
        print("application/pdf")
    elif ".txt" in ftype:
        print("text/plain")
    elif ".zip" in ftype:
        print("application/zip")
    else:
        print("application/octet-stream")



main()
