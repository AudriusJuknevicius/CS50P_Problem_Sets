from datetime import date, timedelta
from num2words import num2words



def main():
    print(date2time(input("Date: ")))


def date2time(userinput):
    birth = date.fromisoformat(userinput)
    today = date.today()
    totaltime = today - birth
    if not totaltime.days <=0:
        return num2words(totaltime.days * 1440)
    raise ValueError("Invalid Input")



if __name__ == "__main__":
    main()
