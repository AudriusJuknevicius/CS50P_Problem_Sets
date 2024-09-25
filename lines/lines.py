import sys

def main():
    if len(sys.argv) != 2: # Checks if it has exactly one in-line argument.
        sys.exit("Too many or few in-line arguments.")

    filename = sys.argv[1] # Identify the file name from the argument.

    if not filename.endswith(".py"): # Checks if the file ends with ".py".
        sys.exit("Not a Python file")

        print(f"Processing file: {filename}") # Continues with the program if the previous two conditions are correct.




    countverified = 0
with open(filename) as file:
    for lines in file:
        linecount = lines.strip()
        if linecount.startswith{"#"}


if __name__ == "__main__":
    main()







#     lambda name, file = sys.argv[1].split(".")
#     if len(sys.argv[1],if file == "py" return True else: sys.exit) >= 1:
#         return sys.argv[1]
#     if file == "py":
#         return True
#     else:
#         sys.exit


#     if len(sys.argv[1],if file == "py" return True else: sys.exit) >= 1:
#         return sys.argv[1]
#         else:
#             sys.exit



# main()
