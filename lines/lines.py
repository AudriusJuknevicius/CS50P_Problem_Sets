import sys

if len(sys.argv) != 2: # Checks if it has exactly one in-line argument.
        sys.exit("Too many or few in-line arguments.")

filename = sys.argv[1] # Identify the file name from the argument.

if not filename.endswith(".py"): # Checks if the file ends with ".py".
        sys.exit("Not a Python file")


with open(filename) as file:
    lines = file.readlines()
    countverified = 0 # Variable to use for counting LOC.
    for line in lines:
        linecount = line.strip() # Strips every line in this loop of spaces.
        if linecount.startswith("#") or len(linecount) == 0: # If line starts with # or nothing, countverified + 0 else +1.
            countverified += 0
        else:
            countverified += 1

    print(countverified) # Prints the LOC.




