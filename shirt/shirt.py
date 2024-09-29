import sys
from PIL import Image, ImageOps

if len(sys.argv) != 3: # Checks if it has exactly one in-line argument.
        sys.exit("Too many or few in-line arguments.")

filename1 = sys.argv[1] # Identify the first file name as the input.
filename2 = sys.argv[2] # Identify the second file name as the output.

if not filename1.lower().endswith((".jpg", ".jpeg", ".png")):  # Checks if the first input has the right file type.
        sys.exit("File must end with .jpeg, .jpeg or .png")

fe1 = filename1.lower().split(".") # Splits filename 1 and 2 to just their extensions.
fe2 = filename2.lower().split(".")

# if not fe1 == fe2:
#         sys.exit("Input extension is not the same as the output's")


person = Image.open(filename1)
shirt = Image.open("shirt.png")

personsize = person.size
shirtsize = shirt.size

person_resized = ImageOps.fit(person, shirt.size)
person_resized.paste(shirt, shirt)
person.save(filename2)





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

