import sys
from PIL import Image

if len(sys.argv) != 3: # Checks if it has exactly one in-line argument.
        sys.exit("Too many or few in-line arguments.")

filename1 = sys.argv[1] # Identify the first file name as the input.
filename2 = sys.argv[2] # Identify the second file name as the output.

if not filename1.lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("File must end with .jpeg, .jpeg or .png")

fe1 = filename1.lower().split(".")
fe2 = filename2.lower().split(".")

if not fe1 == fe2:
        sys.exit("Input extension is not the same as the output's")


image.open(fp: filename1)





# students = []

# try:
#     with open(filename1, "r") as before:
#             reader = csv.DictReader(before)
#             for row in reader:
#                     last, first = row["name"].split(", ")
#                     students.append({"first": first, "last": last, "house": row["house"]})
# except FileNotFoundError:
#     sys.exit("Could not read" + filename1)




# with open(filename2, "w") as after:
#         writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
#         writer.writeheader()
#         for student in students:
#                writer.writerow(student)

