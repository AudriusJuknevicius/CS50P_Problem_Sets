import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", s, re.IGNORECASE)


if matches:
    print(f"Username:", matches.group(2))




if __name__ == "__main__":
    main()
