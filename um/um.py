import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if cases := re.findall(r"\bum\b", s, re.IGNORECASE):
        return len(cases)
    else:
        return 0



if __name__ == "__main__":
    main()
