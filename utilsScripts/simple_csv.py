import csv

# reading a csv file

with open('data.csv', 'rt') as file:
    data = csv.reader(file)
    for row in data:
        print(row)
file.close()

print()
print()

# read csv as dictionary

csvreader = csv.DictReader(open('data.csv'))
for raw in csvreader:
    print(raw)

print()
print()

# Write a csv file

with open('datanew.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(['Programming language', 'Designed by', 'Appeared', 'Extension'])
    writer.writerow(['Python', 'Guido van Rossum', '1991', '.py'])
    writer.writerow(['Java', 'James Gosling', '1995', '.java'])
    writer.writerow(['C++', 'Bjarne Stroustrup', '1985', '.cpp'])

# rechecking data

csvreader = csv.DictReader(open('datanew.csv'))
for raw in csvreader:
    print(raw)
