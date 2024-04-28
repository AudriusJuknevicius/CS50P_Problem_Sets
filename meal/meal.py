# https://cs50.harvard.edu/python/2022/psets/1/meal/
# Implement a program that tells the user if its breakfrast, lunch or dinner time when asked.
# If it's not a meal time, don't output anything at all.


def convert(time):
    hours, minutes = map(float, time.split(":"))
    time_24h = hours + (minutes / 60)
    return time_24h

def main():
    time_input = input("What time is it? ").strip()
    time_24h = convert(time_input)

    if 7.0 <= time_24h <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_24h <= 13.0:
        print("lunch time")
    elif 18.0 <= time_24h <= 19.0:
        print("dinner time")

if __name__ == "__main__":
    main()
