import re
import sys

def main():
        print(convert(input("Hours: ")))

def convert(s):
    # Define regex pattern to match valid input format
    pattern = r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$"

    # Search for the pattern in the input string
    matches = re.match(pattern, s)
    if not matches:
        raise ValueError

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
        raise ValueError

def validate_minutes(minutes1, minutes2):
    if not (0 <= int(minutes1) < 60) or not (0 <= int(minutes2) < 60):
        raise ValueError

if __name__ == "__main__":
    main()
