import sys
from PIL import Image, ImageOps

if len(sys.argv) != 3: # Checks if it has exactly one in-line argument.
        sys.exit("Too many or few in-line arguments.")

filename1 = sys.argv[1] # Identify the first file name as the input.
filename2 = sys.argv[2] # Identify the second file name as the output.

if not filename1.lower().endswith((".jpg", ".jpeg", ".png")):  # Checks if the first input has the right file type.
        sys.exit("File must end with .jpeg, .jpeg or .png")

filename1front, fe1 = filename1.lower().split(".") # Splits filename 1 and 2 to just their extensions.
filename2front, fe2 = filename2.lower().split(".")

if not fe1 == fe2:
        sys.exit("Input extension is not the same as the output's") # Checks input and output extensions.

try:
        person = Image.open(filename1) # Opens before file image.
        shirt = Image.open("shirt.png") # Opens the shirt image file.

        shirtsize = shirt.size # shirtsize variable gains the size information from shirt image file.

        person_resized = ImageOps.fit(person, shirtsize) # 
        person_resized.paste(shirt, shirt)
        person_resized.save(filename2)
except FileNotFoundError:
    sys.exit("Could not read" + filename1)



