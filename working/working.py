import re
import sys

def main():
    # Prompt the user to enter the hours they want to convert
    print(convert(input("Hours: ")))

def convert(s):
    # Define a regex pattern to check for valid time formats
    pattern = r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$"

    # Attempt to match the input against the regex pattern
    matches = re.match(pattern, s)
    if not matches:
        raise ValueError("Invalid time format. Please use the correct format.")

    # Extract hour, minute, and meridiem (AM/PM) components from the matched groups
    hours1, minutes1, meridiem1, hours2, minutes2, meridiem2 = matches.group(1, 2, 3, 4, 5, 6)

    # If minutes are not provided, set them to '00'
    minutes1 = minutes1 or "00"
    minutes2 = minutes2 or "00"

    # Check if the hours are valid (must be between 1 and 12)
    validate_hours(hours1, hours2)

    # Convert both sets of hours to 24-hour format
    hours1_24 = convert_to_24(hours1, meridiem1)
    hours2_24 = convert_to_24(hours2, meridiem2)

    # Validate that the minute values are acceptable
    validate_minutes(minutes1, minutes2)

    # Format and return the final string in 24-hour time
    return f"{hours1_24:02}:{minutes1} to {hours2_24:02}:{minutes2}"

def convert_to_24(hours, meridiem):
    hours = int(hours)
    # Handle the special case for midnight
    if meridiem == "AM" and hours == 12:
        return 0
    # Adjust hours for PM, except for noon
    elif meridiem == "PM" and hours != 12:
        return hours + 12
    return hours

def validate_hours(hours1, hours2):
    # Ensure both hour values are between 1 and 12
    if not (1 <= int(hours1) <= 12) or not (1 <= int(hours2) <= 12):
        raise ValueError("Hours must be between 1 and 12.")

def validate_minutes(minutes1, minutes2):
    # Check that both minute values are within the valid range
    if not (0 <= int(minutes1) < 60) or not (0 <= int(minutes2) < 60):
        raise ValueError("Minutes must be between 0 and 59.")

if __name__ == "__main__":
    main()

