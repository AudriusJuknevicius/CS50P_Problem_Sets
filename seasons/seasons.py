from datetime import date, timedelta
import inflect
p = inflect.engine()

def main():
    print(date2time(input("Date: ")))


def date2time(userinput):
    birth = date.fromisoformat(userinput)
    today = date.today()
    totaltime = today - birth
    if not totaltime.days <=0:
        return p.number_to_words(totaltime.days * 1440, andword="") + " minutes"
    raise ValueError("Invalid Input")



if __name__ == "__main__":
    main()

