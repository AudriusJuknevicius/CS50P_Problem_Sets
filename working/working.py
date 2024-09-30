import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Matches the required format using regex
    if matches := re.match(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s):
        # Extracts the individual groups from regex
        hours1, minutes1, meridiem1 = matches.group(1), matches.group(2), matches.group(3)
        hours2, minutes2, meridiem2 = matches.group(4), matches.group(5), matches.group(6)

        # Sets the default minutes to 00 if None is given
        minutes1 = minutes1 if minutes1 is not None else "00"
        minutes2 = minutes2 if minutes2 is not None else "00"

        # Checks to make sure minutes are within 0-60 range
        if not (0 <= int(minutes1) < 60 and 0 <= int(minutes2) < 60):
            raise ValueError("Invalid minutes")

        # Converts both times to the 24hour range
        time1_24 = f"{convert_to_24(hours1, meridiem1):02}:{minutes1}"
        time2_24 = f"{convert_to_24(hours2, meridiem2):02}:{minutes2}"

        # Returns the formatted 24hour range 
        return f"{time1_24} to {time2_24}"

    # Raise an error if the format does not match
    raise ValueError("Invalid format")

def convert_to_24(hours, meridiem):
    hours = int(hours)
    if meridiem == "AM" and hours == 12:
        return 0  # Midnight case
    elif meridiem == "PM" and hours != 12:
        return hours + 12  # Convert PM to 24-hour time
    return hours

if __name__ == "__main__":
    main()
