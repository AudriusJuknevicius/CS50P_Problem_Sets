import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(.+)\.(.+)\.(.+)\.(.+)$", ip)

    if 0 <= matches.group(1) <= 255:
        return True
    else:
        return False




if __name__ == "__main__":
    main()
