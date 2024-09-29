import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]\.[0-9]\.[0-9]\.[0-9]$", ipv4):
        return ipv4



if __name__ == "__main__":
    main()
