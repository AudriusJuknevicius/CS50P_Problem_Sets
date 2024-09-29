import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)

group1 = int(matches.group(1))

if 0 <= group1 <= 255:
    return True
else:
    return False




if __name__ == "__main__":
    main()
