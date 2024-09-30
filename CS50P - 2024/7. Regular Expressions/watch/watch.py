import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if ":" in s:
        if matches := re.search(r"^ to $")", s, re.IGNORECASE):
            return "https://youtu.be/" + matches.group(2)
        return None

def time_24hrs()
    


if __name__ == "__main__":
    main()

