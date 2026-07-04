import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(f"{row[0]} - {row[2]}")
