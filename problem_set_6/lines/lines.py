import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

user_file = sys.argv[1]

if not user_file.endswith(".py") :
    sys.exit("Not a Python file")

lines_counter = 0
try:
    with open(user_file) as file:
        for line in file:
            stripped_line = line.lstrip()
            if not stripped_line or stripped_line.startswith("#"):
                continue

            lines_counter += 1

    print(f"{lines_counter}")

except FileNotFoundError:
    sys.exit("File does not exist")




