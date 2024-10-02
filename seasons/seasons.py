from datetime import date, timedelta


def main():
    print(date2time(input("Date: ")))


def date2time(userinput):
    return date.fromisoformat(userinput)

def tdelta():
    currenttime = date.today
    seconds = timedelta.total_seconds()


classmethod date.today()


if __name__ == "__main__":
    main()
