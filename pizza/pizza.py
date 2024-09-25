import sys
from tabulate import tabulate

if len(sys.argv) != 2: # Checks if it has exactly one in-line argument.
        sys.exit("Too many or few in-line arguments.")

filename = sys.argv[1] # Identify the file name from the argument.

if not filename.endswith(".csv"): # Checks if the file ends with ".py".
        sys.exit("Not a Comma Seperated Value file")

with open(filename) as pizzycsv:
    pretty = csv.reader(pizzycsv)
    pretty = 
