from datetime import date


def main():
    print(date2time(input("Date: ")))


def date2time(userinput):
    return date.fromisoformat(userinput)




if __name__ == "__main__":
    main()
