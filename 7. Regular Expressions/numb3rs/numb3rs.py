# https://cs50.harvard.edu/python/2022/psets/7/numb3rs/
import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        group1 = int(matches.group(1))
        group2 = int(matches.group(2))
        group3 = int(matches.group(3))
        group4 = int(matches.group(4))
        if 0 <= group1 <= 255 and 0 <= group2 <= 255 and 0 <= group3 <= 255 and 0 <= group4 <= 255:
            return True
    return False



if __name__ == "__main__":
    main()
