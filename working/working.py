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



def convert_to_24(hours, meridiem):
    hours = int(hours)
    if meridiem == "AM" and hours == 12:
        return 0  # Midnight case
    elif meridiem == "PM" and hours != 12:
        return hours + 12  # Convert to 24-hour time for PM, but not for noon
    return hours


if __name__ == "__main__":
    main()

