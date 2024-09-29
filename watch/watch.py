import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if watch := re.sub(r"(.+)https?://(www\.)?youtube\.com/embed/(.+)/(.+)$", "", s, re.IGNORECASE):
        print(watch)
    return False



if __name__ == "__main__":
    main()
