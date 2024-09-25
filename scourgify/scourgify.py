import sys
import csv

if len(sys.argv) != 3: # Checks if it has exactly one in-line argument.
        sys.exit("Too many or few in-line arguments.")

filename1 = sys.argv[1] # Identify the first file name from the argument.
filename2 = sys.argv[2] # Identify the second file name from the argument.

if not filename1.endswith(".csv"): # Checks if the file ends with ".csv".
        sys.exit("Not a Comma Seperated Value file")

students = []

with open(filename1, "r") as before:
        reader = csv.DictReader(before)
        for row in reader:
                students.append({"name": row["name"], "house": row["house"]})



with open(filename2, "w") as after:
        for student in 

