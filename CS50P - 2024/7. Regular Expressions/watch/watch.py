import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$")", s, re.IGNORECASE):
        return matches

def time_24hrs(time)
    hours, minutes = map(float, time.split(":"))
    time_24h = hours + (minutes / 60)
    return time_24h



if __name__ == "__main__":
    main()

