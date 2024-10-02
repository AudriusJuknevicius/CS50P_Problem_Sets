from datetime import date, timedelta
from num2words import num2words



def main():
    print(date2time(input("Date: ")))


def date2time(userinput):
    birth = date.fromisoformat(userinput)
    today = date.today()
    totaltime.days = today - birth
    if not totaltime <=0:
        return num2words(totaltime * 1440))



if __name__ == "__main__":
    main()
