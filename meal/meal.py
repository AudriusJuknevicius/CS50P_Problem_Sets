# https://cs50.harvard.edu/python/2022/psets/1/meal/
# Implement a program that tells the user if its breakfrast, lunch or dinner time when asked.
# If it's not a meal time, don't output anything at all.


def main():
    hours, minutes = convert(input("What time is it? ")).split(":")

def convert(time):
    hours = float(time)
    minutes = float((time - hours) * 60)
    return hours, minutes


print(hours, minutes)


# if __name__ == "__main__":
#     main()

main()
