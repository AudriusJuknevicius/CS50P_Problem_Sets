import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"(.+)youtube\.com/embed/(/w)/W(.+)", s, re.IGNORECASE):
        print(match.group(2))
    return False



if __name__ == "__main__":
    main()
