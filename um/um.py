import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    cases = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(cases)



if __name__ == "__main__":
    main()
