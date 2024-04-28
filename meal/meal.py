# https://cs50.harvard.edu/python/2022/psets/1/meal/
# Implement a program that tells the user if its breakfrast, lunch or dinner time when asked.
# If it's not a meal time, don't output anything at all.


def convert(time):
    hours, minutes = float(time.split(":"))
    time_24h = hours + (minutes / 60)
    return time_24h

def main():
    time_input = input("What time is it? ")
    time_24h = convert(time_input)

    if 

    # def convert(time):
    # hours, minutes = time.split(":")
    # hours = float(hours)
    # minutes = float((time - hours) * 60)

    # time_24h = hours + minutes

    # return time_24h


# if __name__ == "__main__":
#     main()

main()
