# import re

# def main():
#     print(convert(input("Hours: ")))

# def convert(s):
#     # Matches the required format using regex
#     if matches := re.match(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s):
#         # Extracts the individual groups from regex
#         hours1, minutes1, meridiem1 = matches.group(1), matches.group(2), matches.group(3)
#         hours2, minutes2, meridiem2 = matches.group(4), matches.group(5), matches.group(6)

#         # Sets the default minutes to 00 if None is given
#         minutes1 = minutes1 if minutes1 is not None else "00"
#         minutes2 = minutes2 if minutes2 is not None else "00"

#         # Checks to make sure minutes are within 0-60 range
#         if not (0 <= int(minutes1) < 60 and 0 <= int(minutes2) < 60):
#             raise ValueError("Invalid minutes")

#         # Converts both times to the 24hour range
#         time1_24 = f"{convert_to_24(hours1, meridiem1):02}:{minutes1}"
#         time2_24 = f"{convert_to_24(hours2, meridiem2):02}:{minutes2}"

#         # Returns the formatted 24hour range
#         return f"{time1_24} to {time2_24}"

#     # Raise an error if the format does not match
#     raise ValueError("Invalid format")

# def convert_to_24(hours, meridiem):
#     hours = int(hours)
#     if meridiem == "AM" and hours == 12:
#         return 0  # Midnight case
#     elif meridiem == "PM" and hours != 12:
#         return hours + 12  # Convert PM to 24-hour time
#     return hours

# if __name__ == "__main__":
#     main()



import re
import sys

def main():
    # Prompt user for input and convert the time
    try:
        print(convert(input("Hours: ")))
    except ValueError

def convert(s):
    # Define regex pattern to match valid input format
    pattern = r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$"

    # Search for the pattern in the input string
    matches = re.match(pattern, s)
    if not matches:
        raise ValueError("Invalid input format")

    # Extract components from regex groups
    hours1, minutes1, meridiem1, hours2, minutes2, meridiem2 = matches.group(1, 2, 3, 4, 5, 6)

    # Default minutes to '00' if not provided
    minutes1 = minutes1 or "00"
    minutes2 = minutes2 or "00"

    # Validate hours (should be between 1 and 12)
    validate_hours(hours1, hours2)

    # Convert hours1 and hours2 to 24-hour format
    hours1_24 = convert_to_24(hours1, meridiem1)
    hours2_24 = convert_to_24(hours2, meridiem2)

    # Check for invalid minute values
    validate_minutes(minutes1, minutes2)

    # Return formatted 24-hour string
    return f"{hours1_24:02}:{minutes1} to {hours2_24:02}:{minutes2}"

def convert_to_24(hours, meridiem):
    hours = int(hours)
    if meridiem == "AM" and hours == 12:
        return 0  # Midnight case
    elif meridiem == "PM" and hours != 12:
        return hours + 12  # Convert to 24-hour time for PM, except for noon
    return hours

def validate_hours(hours1, hours2):
    if not (1 <= int(hours1) <= 12) or not (1 <= int(hours2) <= 12):
        raise ValueError("Invalid hour value")

def validate_minutes(minutes1, minutes2):
    if not (0 <= int(minutes1) < 60) or not (0 <= int(minutes2) < 60):
        raise ValueError("Invalid minute value")

if __name__ == "__main__":
    main()
