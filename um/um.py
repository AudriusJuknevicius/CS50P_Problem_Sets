import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if cases := re.findall(r".+\w+um\.+", s, re.IGNORECASE):
        return cases


...


if __name__ == "__main__":
    main()
