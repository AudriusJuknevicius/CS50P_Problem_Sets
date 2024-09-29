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
        try:
            if 0 <= group1 <= 255:
                return True
            else:
                return False
    return False




if __name__ == "__main__":
    main()
