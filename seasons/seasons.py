import inflect
import sys
from datetime import date, timedelta
p = inflect.engine()

def main():
    print(date2time(input("Date: ")))


def date2time(userinput):
    if not birth = date.fromisoformat(userinput):
        sys.exit()
        today = date.today()
        totaltime = today - birth
        if not totaltime.days <=0:
            return str.capitalize((p.number_to_words(totaltime.days * 1440, andword="") + " minutes"))
        else:
            sys.exit()



if __name__ == "__main__":
    main()

