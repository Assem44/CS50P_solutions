import sys, csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

old_file = sys.argv[1]
new_file = sys.argv[2]

students = []

try:
    with open(old_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last_name, first_name = row['name'].split(', ')

            students.append(
                {
                    "first" : first_name,
                    "last" : last_name,
                    "house" : row['house'],
                }
            )
    with open(new_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)

except FileNotFoundError:
    sys.exit(f"Could not read {old_file}")





