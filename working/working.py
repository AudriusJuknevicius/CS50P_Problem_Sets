import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"(https?)://(?:www\.)?youtube\.com/embed/(\w+)", s, re.IGNORECASE):
if matches:
    print(f"Username:", matches.group(2))


if __name__ == "__main__":
    main()
