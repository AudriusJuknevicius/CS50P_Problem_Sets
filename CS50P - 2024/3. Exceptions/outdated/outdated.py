# https://cs50.harvard.edu/python/2022/psets/3/outdated/

def main():

    fmonths = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    while True:
        try:
            userdate = input("Date: ")
            if "/" in userdate:
                answer2 = numcheck(userdate)
                if answer2 is not False:
                    year, month, day = answer2
                    date = "{:04d}-{:02d}-{:02d}".format(year, month, day)
                    print(date)
                    break
            elif letcheck(userdate, fmonths):
                answer1 = letcheck(userdate, fmonths)
                if answer1 is not False:
                    year, month, day = answer1
                    date = "{:04d}-{:02d}-{:02d}".format(year, month, day)
                    print(date)
                    break

        except KeyboardInterrupt:
            print("/nExiting Program....")
            break

def letcheck(lc, fmonths):
    if "," in lc:
        lc = lc.replace(",","")
        mm, dd, yyyy = lc.split(sep=" ")
        if mm.isalpha() and dd.isdigit():
            dd = int(dd)
            if dd >31:
                return False
            yyyy = int(yyyy)
            if mm in fmonths:
                monthnumber = fmonths[mm]
                if monthnumber >12:
                    return False
                return yyyy, monthnumber, dd
            return False
        return False
    return False

def numcheck(nc):
      nc = nc.strip()
      mm, dd, yyyy = nc.split(sep="/")
      if dd.isdigit() and mm.isdigit():
        mm = int(mm)
        if mm >12:
          return False
        dd = int(dd)
        if dd >31:
            return False
        else:
            yyyy = int(yyyy)
            return yyyy, mm, dd
      return False

main()

