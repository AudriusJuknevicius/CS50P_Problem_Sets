import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if "src" in s:
        if matches := re.search(r"(https?)://(?:www\.)?youtube\.com/embed/(\w+)", s, re.IGNORECASE):
            return "https://youtu.be/" + matches.group(2)
        return None



if __name__ == "__main__":
    main()

