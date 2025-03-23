import inflect
import sys
from datetime import date, timedelta
p = inflect.engine()

def main():
    print(date2time(input("Date: ")))


def date2time(userinput):
    try:
        birth = date.fromisoformat(userinput)
    except ValueError:
        sys.exit("Invalid date format. Please use YYYY-MM-DD.")

    today = date.today()
    totaltime = today - birth

    if totaltime.days > 0:
        return str.capitalize((p.number_to_words(totaltime.days * 1440, andword="") + " minutes"))
    else:
        sys.exit("Invalid Date. The date must be in the past")



if __name__ == "__main__":
    main()

