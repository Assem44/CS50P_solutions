from tabulate import tabulate
import sys, csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

user_file = sys.argv[1]

if not user_file.endswith(".csv") :
    sys.exit("Not a CSV file")

try:
    with open(user_file) as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
