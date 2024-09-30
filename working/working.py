import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE):
        hours1 = matches.group(1)
        minutes1 = matches.group(2)
        meridiem1 = matches.group(3)
        hours2 = matches.group(4)
        minutes2 = matches.group(5)
        meridiem2 = matches.group(6)



def check_minutes():
    if 








def time_24hrs(time)
    hours, minutes = map(float, time.split(":"))
    time_24h = hours + (minutes / 60)
    return time_24h



if __name__ == "__main__":
    main()

