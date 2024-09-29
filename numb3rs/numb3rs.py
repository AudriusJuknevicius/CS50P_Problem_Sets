import re
import sys


def main():
    ipv4 = print(validate(input("IPv4 Address: ")))


def validate(ip):
matches = re.search(r"^(.+)\.(.+)\.(.+)\.(.+)$", ip)






if __name__ == "__main__":
    main()
