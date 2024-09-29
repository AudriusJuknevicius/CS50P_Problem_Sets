import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"youtube\.com/embed/(\w+)", s, re.IGNORECASE):
        print("https://youtu.be/"+match.group(1))
    return False



if __name__ == "__main__":
    main()
